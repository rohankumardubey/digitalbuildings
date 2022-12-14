# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Unit document used for creating fake unit universe."""

UNIT_DOCUMENT = {
    'concentration': [{
        'parts_per_million': 'STANDARD'
    }],
    'current': [{
        'amperes': 'STANDARD'
    }, 'milliamperes'],
    'energy': [{
        'joules': 'STANDARD'
    }, 'kilowatt_hours'],
    'flowrate': [{
        'cubic_meters_per_second': 'STANDARD'
    }, 'cubic_feet_per_minute', 'gallons_per_minute', 'liters_per_second'],
    'frequency': [{
        'hertz': 'STANDARD'
    }],
    'humidity': [{
        'percent_relative_humidity': 'STANDARD'
    }],
    'illuminance': [{
        'lux': 'STANDARD'
    }],
    'level': [{
        'meters': 'STANDARD'
    }, 'feet'],
    'linearvelocity': [{
        'meters_per_second': 'STANDARD'
    }, 'feet_per_minute', 'miles_per_hour'],
    'percentage': [{
        'percent': 'STANDARD'
    }],
    'powerfactor': [{
        'no_units': 'STANDARD'
    }],
    'power': [{
        'watts': 'STANDARD'
    }, 'kilowatts', 'tons_of_refrigeration', 'kilovolt_amperes',
              'kilovolt_amperes_reactive'],
    'pressure': [{
        'pascals': 'STANDARD'
    }, 'inches_of_water', 'pounds_force_per_square_inch'],
    'resistance': [{
        'ohms': 'STANDARD'
    }, 'kiloohms'],
    'specificenthalpy': [{
        'joules_per_kilogram': 'STANDARD'
    }, 'btus_per_pound_dry_air'],
    'temperature': [{
        'kelvins': 'STANDARD'
    }, 'degrees_celsius', 'degrees_fahrenheit'],
    'voltage': [{
        'volts': 'STANDARD'
    }],
    'volume': [{
        'cubic_meters': 'STANDARD'
    }, 'us_gallons']
}
