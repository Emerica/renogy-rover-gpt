"""Support for the Renogy Rover load switch."""

import logging

from homeassistant.components.switch import SwitchEntity
from homeassistant.const import ATTR_ENTITY_ID
from homeassistant.core import callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.event import async_call_later

from .const import (
    DOMAIN,
    LOGGER,
    SIGNAL_UPDATE_ROVER,
    SERVICE_SET_LOAD,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Renogy Rover switch."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([RenogyRoverSwitch(coordinator)], True)


class RenogyRoverSwitch(SwitchEntity):
    """Representation of a Renogy Rover load switch."""

    def __init__(self, coordinator):
        """Initialize the switch."""
        self._name = f"{coordinator.rover.alias} Load Switch"
        self._coordinator = coordinator
        self._is_on = None

    async def async_added_to_hass(self):
        """Register callbacks when entity is added."""
        self.async_on_remove(
            async_dispatcher_connect(
                self.hass, SIGNAL_UPDATE_ROVER, self._update_callback
            )
        )

    async def async_update(self):
        """Fetch the latest data and update the switch."""
        await self._coordinator.async_request_refresh()

    @callback
    def _update_callback(self):
        """Update the switch state."""
        self._is_on = self._coordinator.rover.load_status == "on"
        self.async_write_ha_state()

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def is_on(self):
        """Return the current state of the switch."""
        return self._is_on

    async def async_turn_on(self, **kwargs):
        """Turn the switch on."""
        data = {ATTR_ENTITY_ID: self.entity_id, "load": 1}
        await self.hass.services.async_call(DOMAIN, SERVICE_SET_LOAD, data)
        self._is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn the switch off."""
        data = {ATTR_ENTITY_ID: self.entity_id, "load": 0}
        await self.hass.services.async_call(DOMAIN, SERVICE_SET_LOAD, data)
        self._is_on = False
        self.async_write_ha_state()

    @property
    def should_poll(self):
        """Return the polling state."""
        return False

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return "mdi:electric-switch"
