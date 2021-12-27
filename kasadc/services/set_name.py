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

from util import KasaDevice


async def handle_set_name(device: KasaDevice, payload: dict, *args, **kwargs):
    if "name" not in payload:
        raise RuntimeError("Missing name in payload")
    return await device.get_kasa().set_alias(payload["name"])
