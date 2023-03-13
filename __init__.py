import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
    CONF_PORT,
)
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType

from renogy_rover import BTOneApp
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the Renogy Rover from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    host = entry.data.get(CONF_HOST)
    port = entry.data.get(CONF_PORT)
    name = entry.data.get(CONF_NAME)

    rover = RenogyRover(hass, host, port, name)
    if not await rover.async_setup():
        raise ConfigEntryNotReady

    hass.data[DOMAIN][entry.entry_id] = rover
    entry.async_on_unload(rover.async_unload)

    return True


class RenogyRover:
    def __init__(self, hass: HomeAssistant, host: str, port: int, name: str):
        self.hass = hass
        self.host = host
        self.port = port
        self.name = name
        self.bt_app = None

    async def async_setup(self) -> bool:
        """Set up the Renogy Rover integration."""
        self.bt_app = BTOneApp(self.host, self.port, self.name)
        if not await self.hass.async_add_executor_job(self.bt_app.connect):
            _LOGGER.error("Unable to connect to Renogy Rover at %s:%s", self.host, self.port)
            return False

        return True

    async def async_unload(self) -> None:
        """Unload the Renogy Rover integration."""
        if self.bt_app is not None:
            self.bt_app.disconnect()

        self.hass.data[DOMAIN].pop(self.entry_id)

    def get_sensors(self):
        """Get the sensor data from the Renogy Rover."""
        return self.bt_app.get_sensor_data()

    def set_load(self, load: bool):
        """Set the load status of the Renogy Rover."""
        self.bt_app.set_load(load)