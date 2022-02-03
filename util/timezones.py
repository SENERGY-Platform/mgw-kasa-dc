"""
   Copyright 2022 InfAI (CC SES)

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
import datetime, pytz

timezones = [
    'Etc/GMT+11',
    'America/Adak',
    'America/Anchorage',
    'America/Santa_Isabel',
    'America/Metlakatla',
    'America/Dawson',
    'America/Phoenix',
    'America/Chihuahua',
    'America/Creston',
    'America/Boise',
    'America/Bahia_Banderas',
    'America/Belize',
    'America/Chicago',
    'America/Matamoros',
    'America/Regina',
    'America/Bogota',
    'America/Atikokan',
    'America/Cancun',
    'America/Fort_Wayne',
    'America/Caracas',
    'America/Asuncion',
    'America/Anguilla',
    'America/Glace_Bay',
    'America/Campo_Grande',
    'America/Boa_Vista',
    'America/Santiago',
    'America/St_Johns',
    'America/Sao_Paulo',
    'America/Argentina/Buenos_Aires',
    'America/Cayenne',
    'America/Godthab',
    'America/Montevideo',
    'America/Araguaina',
    'America/Noronha',
    'America/Scoresbysund',
    'Atlantic/Cape_Verde',
    'Africa/Casablanca',
    'Africa/Abidjan',
    'Europe/Belfast',
    'Africa/Monrovia',
    'Europe/Berlin',
    'Europe/Belgrade',
    'Africa/Ceuta',
    'Europe/Ljubljana',
    'Africa/Algiers',
    'Africa/Windhoek',
    'Asia/Amman',
    'Europe/Athens',
    'Asia/Beirut',
    'Africa/Cairo',
    'Asia/Damascus',
    'EET',
    'Africa/Blantyre',
    'Europe/Helsinki',
    'Asia/Istanbul',
    'Asia/Gaza',
    'Europe/Kaliningrad',
    'Africa/Tripoli',
    'Asia/Baghdad',
    'Asia/Aden',
    'Europe/Minsk',
    'Etc/GMT-3',
    'Africa/Addis_Ababa',
    'Asia/Tehran',
    'Asia/Dubai',
    'Asia/Baku',
    'Europe/Samara',
    'Indian/Mauritius',
    'Asia/Tbilisi',
    'Asia/Yerevan',
    'Asia/Kabul',
    'Asia/Ashgabat',
    'Antarctica/Mawson',
    'Asia/Aqtau',
    'Asia/Kolkata',
    'Asia/Colombo',
    'Asia/Kathmandu',
    'Asia/Almaty',
    'Asia/Dacca',
    'Antarctica/Vostok',
    'Asia/Rangoon',
    'Asia/Bangkok',
    'Antarctica/Davis',
    'Asia/Chongqing',
    'Asia/Irkutsk',
    'Asia/Brunei',
    'Antarctica/Casey',
    'Asia/Taipei',
    'Asia/Choibalsan',
    'Asia/Dili',
    'Asia/Pyongyang',
    'Asia/Chita',
    'Australia/Adelaide',
    'Australia/Darwin',
    'Australia/Brisbane',
    'Australia/ACT',
    'Pacific/Chuuk',
    'Australia/Hobart',
    'Antarctica/DumontDUrville',
    'Asia/Ust-Nera',
    'Asia/Srednekolymsk',
    'Antarctica/Macquarie',
    'Asia/Anadyr',
    'Antarctica/McMurdo',
    'Etc/GMT-12',
    'Pacific/Fiji',
    'Etc/GMT-13',
    'Pacific/Apia',
    'Etc/GMT-14',
]


def localize_time(time: datetime.datetime, zoneIndex: int) -> datetime.datetime:
    return pytz.timezone(timezones[zoneIndex]).localize(time)


if __name__ == "__main__":
    for tz in timezones:
        try:
            datetime.datetime.now(pytz.timezone(tz)).strftime('%z')
        except Exception as e:
            print("Problem with timezone: " + str(e))
