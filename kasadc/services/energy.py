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

import rfc3339

from util import KasaDevice
from util.timezones import localize_time


async def handle_energy(device: KasaDevice, *args, **kwargs) -> typing.Dict:
    kasa = device.get_kasa()

    await kasa.update()
    time = await kasa.get_time()
    if time is not None:
        tz = await kasa.get_timezone()
        time = localize_time(time, tz['index'])
    resp = {
        "on": kasa.is_on,
        "current": kasa.emeter_realtime.current,
        "power": kasa.emeter_realtime.power,
        "total": kasa.emeter_realtime.total,
        "voltage": kasa.emeter_realtime.voltage,
        "today": kasa.emeter_today,
        "month": kasa.emeter_this_month,
        "time": rfc3339.format(time, utc=True)
    }
    return resp
