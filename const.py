DOMAIN = 'renogy_bt1'

CONF_DEVICE_ID = 'device_id'
CONF_DEVICE_NAME = 'device_name'
CONF_SCAN_TIMEOUT = 'scan_timeout'

DEFAULT_SCAN_TIMEOUT = 10

CONFIG_FILE = 'renogy_bt1_config.yaml'

DATA_CLIENT = 'client'

MANUFACTURER = 'Renogy'

SENSOR_TYPES = {
    'battery_voltage': ['Battery Voltage', 'V', 'battery_volt', MANUFACTURER],
    'battery_temperature': ['Battery Temperature', '°C', 'battery_temp', MANUFACTURER],
    'pv_voltage': ['PV Voltage', 'V', 'pv_volt', MANUFACTURER],
    'pv_current': ['PV Current', 'A', 'pv_current', MANUFACTURER],
    'pv_watts': ['PV Power', 'W', 'pv_watts', MANUFACTURER],
    'load_voltage': ['Load Voltage', 'V', 'load_volt', MANUFACTURER],
    'load_current': ['Load Current', 'A', 'load_current', MANUFACTURER],
    'load_watts': ['Load Power', 'W', 'load_watts', MANUFACTURER],
    'charging_power': ['Charging Power', 'W', 'charging_power', MANUFACTURER],
    'charging_current': ['Charging Current', 'A', 'charging_current', MANUFACTURER],
    'charging_mode': ['Charging Mode', '', 'charging_mode', MANUFACTURER],
    'battery_capacity': ['Battery Capacity', '%', 'battery_capacity', MANUFACTURER],
    'charge_status': ['Charge Status', '', 'charge_status', MANUFACTURER],
    'faults': ['Faults', '', 'faults', MANUFACTURER],
    'errors': ['Errors', '', 'errors', MANUFACTURER],
}

DEVICE_TYPES = {
    'rover': 'Rover',
    'commander': 'Commander',
    'wanderer': 'Wanderer',
    'adventurer': 'Adventurer',
    'tracer': 'Tracer',
    'tracer_duo': 'Tracer Duo',
    'tracer_bn': 'Tracer BN',
    'mt50': 'MT50',
    'rnd': 'RND'
}