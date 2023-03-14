# DONT USE THIS - IT'S JUST AN EXPERIMENT TO SEE IF GPT CAN BUILD INTEGRATIONS


# Renogy Rover Solar Charge Controller Component for Home Assistant

This is a custom component for [Home Assistant](https://www.home-assistant.io/) that integrates with the Renogy Rover solar charge controller using the Renogy Bluetooth Module BT-1.

## Installation

Copy the `renogy_rover_gpt` directory and its contents to the `custom_components` directory in your Home Assistant configuration directory. For example:


config/custom_components/renogy_rover_gpt/







## Configuration

Add the following to your Home Assistant `configuration.yaml` file:

```yaml
sensor:
  - platform: renogy_rover_gpt
    port: '/dev/ttyUSB0'  # or the address of the BT-1 module
    scan_interval: 30
    monitored_conditions:
      - charging_state
      - battery_voltage
      - battery_temperature
      - load_on
      - load_current
      - solar_input_voltage
      - solar_input_current
      - battery_capacity
      - battery_full_voltage
      - battery_empty_voltage
      - controller_temperature

switch:
  - platform: renogy_rover_gpt
    port: '/dev/ttyUSB0'  # or the address of the BT-1 module
    scan_interval: 30
    switches:
      - name: "Load"
        switch_type: "load"
      - name: "Manual"
        switch_type: "manual"




Configuration Variables
port (string) (Required): The serial port or Bluetooth MAC address of the BT-1 module.
scan_interval (int) (Optional): The time in seconds between updates. Default is 30 seconds.
monitored_conditions (list) (Optional): The list of conditions to monitor. If not specified, all conditions will be monitored.
switches (list) (Optional): The list of switches to create. If not specified, no switches will be created.
Monitored Conditions
charging_state: Charging state of the battery (charging, discharging, or floating).
battery_voltage: Battery voltage in volts (V).
battery_temperature: Battery temperature in degrees Celsius (°C).
load_on: Whether the load is on (true or false).
load_current: Load current in amps (A).
solar_input_voltage: Solar panel voltage in volts (V).
solar_input_current: Solar panel current in amps (A).
battery_capacity: Battery capacity remaining as a percentage (%).
battery_full_voltage: Battery voltage when fully charged in volts (V).
battery_empty_voltage: Battery voltage when empty in volts (V).
controller_temperature: Charge controller temperature in degrees Celsius (°C).
Switch Types
load: A switch to turn the load on and off.
manual: A switch to toggle the charge controller between manual and automatic mode.
Credits
This custom component was created by GPT and improved by Emerica using the Renogy BT-1 Library.

This project is licensed under the MIT license.
