# Renogy Rover Home Assistant Integration

This integration allows Home Assistant to communicate with Renogy Rover solar charge controllers using the Modbus RTU protocol. The integration provides sensors for various data points as well as a switch to turn the load on and off.

## Installation

1. Copy the `custom_components` directory into the `config` directory of your Home Assistant installation. If the `custom_components` directory does not exist, create it.
2. Add the following to your `configuration.yaml` file:

    ```
    renogy_rover:
      type: serial
      device: /dev/ttyUSB0
      baud: 9600
      scan_interval: 10
      name: My Renogy Rover
    ```

    Replace `/dev/ttyUSB0` with the path to your serial device, and adjust the `baud` rate and `scan_interval` to your needs. You can also change the `name` to whatever you like.

3. Restart Home Assistant.

## Configuration

The following configuration options are available:

- `type` (required): The type of connection to use. Currently, only `serial` is supported.
- `device` (required): The path to the serial device to use.
- `baud` (required): The baud rate to use.
- `scan_interval` (optional, default=10): The number of seconds between updates.
- `name` (optional, default='Renogy Rover'): The name of the Renogy Rover.

## Supported sensors

The following sensors are supported:

- Battery Voltage (`battery_voltage`)
- Battery Temperature (`battery_temperature`)
- Charging Current (`charging_current`)
- Charging Power (`charging_power`)
- Load Current (`load_current`)
- Load Power (`load_power`)
- Load Status (`load_status`)
- PV Voltage (`pv_voltage`)
- PV Current (`pv_current`)
- PV Power (`pv_power`)

## Switch

The following switch is supported:

- Load Switch (`load_switch`)

## Contributions

Contributions are welcome! Please open an issue or pull request on the GitHub repository.

## Credits

- Renogy for producing the Renogy Rover and providing documentation on the Modbus RTU protocol
- ChatGPT for writing this README file