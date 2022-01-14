"""
   Copyright 2021 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import asyncio
import ipaddress
import threading
import time
from typing import Dict, Tuple, List

import kasa
from kasa import Discover, SmartDeviceException
from mgw_dc.dm import device_state

from util import get_logger, conf, diff, init_logger, KasaDevice

__all__ = ("Discovery",)

from util.device_manager import DeviceManager
from util.scanner import Scanner

logger = get_logger(__name__.split(".", 1)[-1])


class Discovery(threading.Thread):
    def __init__(self, device_manager: DeviceManager):
        super().__init__(name="discovery", daemon=True)
        self._device_manager = device_manager

    @staticmethod
    async def get_kasa_devices() -> Dict[str, KasaDevice]:
        logger.info("Starting scan")
        devices: Dict[str, KasaDevice] = {}

        subnet = ipaddress.ip_network(conf.Discovery.subnet)
        host_port: List[Tuple[str, int]] = []
        for host in subnet:
            host_port.append((str(host), conf.Discovery.tcp_port))

        host_port = Scanner.scan(host_port=host_port, num_workers=conf.Discovery.num_workers,
                                 timeout=conf.Discovery.timeout)

        hosts = str(conf.Discovery.ip_list).split(',')
        for host, _ in host_port:
            hosts.append(host)

        unique_hosts: Dict[str, any] = {}
        for host in hosts:
            unique_hosts[host] = {}

        devs: Dict[str, kasa.SmartDevice] = {}
        for ip in unique_hosts.keys():
            if len(ip) == 0: continue
            try:
                dev = await Discover.discover_single(ip)
                devs[ip] = dev
            except SmartDeviceException as e:
                logger.warning("Could not discover device with ip " + ip)
        for addr, dev in devs.items():
            if not dev.is_plug:
                logger.warning("Found Kasa device that is not a plug. Device will be ignored, since not implemented")
                logger.debug(str(dev))
                continue
            logger.info("Discovered '" + dev.alias + "' at " + dev.host)
            id = conf.Discovery.device_id_prefix + dev.device_id
            attributes = [
                {"key": "network/mac", "value": dev.mac},
                {"key": "network/ip", "value": dev.host},
                {"key": "kasa/sw_ver", "value": dev.hw_info["sw_ver"]},
                {"key": "kasa/hw_ver", "value": dev.hw_info["hw_ver"]},
                {"key": "kasa/hw_id", "value": dev.hw_info["hwId"]},
                {"key": "kasa/oem_id", "value": dev.hw_info["oemId"]},
                {"key": "kasa/model", "value": dev.model},
                {"key": "location/latitude", "value": str(dev.location["latitude"])},
                {"key": "location/longitude", "value": str(dev.location["longitude"])},
            ]
            if "fwId" in dev.hw_info:
                attributes.append({"key": "kasa/fw_id", "value": dev.hw_info["fwId"]})
            devices[id] = KasaDevice(id=id, name=dev.alias, type=conf.Senergy.dt_plug, state=device_state.online,
                                     kasa_device=dev, attributes=attributes)

        logger.info("Discovered " + str(len(devices)) + " devices")
        return devices

    async def _refresh_devices(self):
        try:
            kasa_devices = await self.get_kasa_devices()
            stored_devices = self._device_manager.get_devices()

            new_devices, missing_devices, existing_devices = diff(stored_devices, kasa_devices)
            if new_devices:
                for device_id in new_devices:
                    self._device_manager.handle_new_device(kasa_devices[device_id])
            if missing_devices:
                for device_id in missing_devices:
                    self._device_manager.handle_missing_device(stored_devices[device_id])
            if existing_devices:
                for device_id in existing_devices:
                    self._device_manager.handle_existing_device(stored_devices[device_id])
            self._device_manager.set_devices(devices=kasa_devices)
        except Exception as ex:
            logger.error("refreshing devices failed - {}".format(ex))

    def run(self) -> None:
        logger.info("starting {} ...".format(self.name))
        asyncio.run(self.discovery_loop())

    async def discovery_loop(self):
        await self._refresh_devices()
        last_discovery = time.time()
        while True:
            if time.time() - last_discovery > conf.Discovery.scan_delay:
                last_discovery = time.time()
                await self._refresh_devices()
            time.sleep(conf.Discovery.scan_delay / 100)  # at most 1 % too late


if __name__ == "__main__":
    init_logger("debug")
    discovery = Discovery(device_manager=None)
    discovery.get_kasa_devices()
