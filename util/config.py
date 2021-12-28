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

__all__ = ("conf",)

import simple_env_var


@simple_env_var.configuration
class Conf:
    @simple_env_var.section
    class MsgBroker:
        host = "message-broker"
        port = 1883

    @simple_env_var.section
    class Logger:
        level = "debug"
        enable_mqtt = False

    @simple_env_var.section
    class Client:
        clean_session = False
        keep_alive = 30
        id = "kasa-dc"

    @simple_env_var.section
    class Discovery:
        scan_delay = 1800
        timeout = 2
        subnet = '10.42.0.0/24'
        tcp_port = 9999
        num_workers = 0
        ip_list = ""
        device_id_prefix = "kasa-"

    @simple_env_var.section
    class StartDelay:
        enabled = False
        min = 5
        max = 20

    @simple_env_var.section
    class Senergy:
        dt_plug = "urn:infai:ses:device-type:619c53c4-8f47-460f-b42d-50297a0f16a5"
        service_status = "status"
        service_energy = "energy"
        service_set_on_off = "set_on_off"
        service_set_on = "set_on"
        service_set_off = "set_off"
        service_set_led = "set_led"
        service_set_led_on = "set_led_on"
        service_set_led_off = "set_led_off"
        service_set_name = "set_name"
        service_reboot = "reboot"
        events_status_seconds = 600
        events_energy_seconds = 30

conf = Conf()

if not conf.Senergy.dt_plug:
    exit('Please provide SENERGY device types')
