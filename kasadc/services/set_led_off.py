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

import kasa

from util import KasaDevice


async def handle_set_led_off(device: KasaDevice, *args, **kwargs):
    k = device.get_kasa()
    if not isinstance(k, kasa.SmartPlug):
        raise RuntimeError("Device is not a switch")
    return await k.set_led(False)

