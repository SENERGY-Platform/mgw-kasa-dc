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

import mgw_dc.dm
from kasa import SmartDevice

__all__ = ("KasaDevice",)


class KasaDevice(mgw_dc.dm.Device):
    def __init__(self, id: str, name: str, type: str, kasa_device: SmartDevice, state: typing.Optional[str] = None,
                 attributes=None):
        super().__init__(id, name, type, state, attributes)
        self._kasa_device = kasa_device

    def get_kasa(self) -> SmartDevice:
        return self._kasa_device
