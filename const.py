DOMAIN = "renogy_rover"
DEFAULT_NAME = "Renogy Rover"
DEFAULT_SCAN_INTERVAL = timedelta(minutes=5)

SENSOR_TYPES = {
    "battery_voltage": ["Battery Voltage", "V", "mdi:flash-triangle", "voltage"],
    "load_voltage": ["Load Voltage", "V", "mdi:flash-triangle", "voltage"],
    "pv_voltage": ["PV Voltage", "V", "mdi:flash-triangle", "voltage"],
    "controller_temperature": ["Controller Temperature", "°C", "mdi:thermometer", "temperature"],
    "battery_temperature": ["Battery Temperature", "°C", "mdi:thermometer", "temperature"],
    "load_status": ["Load Status", "", "mdi:electric-switch", "outlet"],
    "load_power": ["Load Power", "W", "mdi:lightning-bolt-circle", "power"],
    "pv_power": ["PV Power", "W", "mdi:lightning-bolt-circle", "power"],
    "max_charging_power_today": ["Max Charging Power Today", "W", "mdi:lightning-bolt-circle", "power"],
    "max_discharging_power_today": ["Max Discharging Power Today", "W", "mdi:lightning-bolt-circle", "power"],
    "power_generation_today": ["Power Generation Today", "W", "mdi:lightning-bolt-circle", "power"],
    "power_generation_total": ["Power Generation Total", "W", "mdi:lightning-bolt-circle", "power"],
    "load_current": ["Load Current", "A", "mdi:lightning-bolt-circle", "current"],
    "pv_current": ["PV Current", "A", "mdi:lightning-bolt-circle", "current"],
    "charging_amp_hours_today": ["Charging Amp Hours Today", "Ah", "mdi:lightning-bolt-circle", "current"],
    "discharging_amp_hours_today": ["Discharging Amp Hours Today", "Ah", "mdi:lightning-bolt-circle", "current"],
    "charging_status": ["Charging Status", "", "mdi:electric-switch", ""],
    "battery_percentage": ["Battery Percentage", "%", "mdi:battery", "battery"],
}