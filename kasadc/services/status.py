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
import typing

import kasa

from util import KasaDevice


async def handle_status(device: KasaDevice, *args, **kwargs) -> typing.Dict:
    k = device.get_kasa()
    if not isinstance(k, kasa.SmartPlug):
        raise RuntimeError("Device is not a switch")

    await device.get_kasa().update()
    time = await k.get_time()

    resp = {
        "mac": k.mac,
        "ip": k.host,
        "sw_ver": k.hw_info["sw_ver"],
        "hw_ver": k.hw_info["hw_ver"],
        "hw_id": k.hw_info["hwId"],
        "oem_id": k.hw_info["oemId"],
        "model": k.model,
        "rssi": k.rssi,
        "location": k.location,
        "led_enabled": k.led,
        "time": str(time),
    }
    if "fwId" in k.hw_info:
        resp["fw_id"] = k.hw_info["fwId"]
    return resp
