"""Support for Renogy Rover Charge Controllers."""
from __future__ import annotations

from typing import Any, Optional

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_ID,
    CONF_NAME,
    CONF_SCAN_INTERVAL,
    DEVICE_CLASS_OUTLET,
    DEVICE_CLASS_SWITCH,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

from .const import (
    CONF_SENSOR_TYPE,
    DEFAULT_NAME,
    DOMAIN,
    ICON,
    SENSOR_TYPES,
    SWITCH_TYPES,
)
from .coordinator import RenogyDataUpdateCoordinator
from .helpers import (
    RenogyDeviceEntity,
    RenogyEntityDescription,
    async_get_renogy_device_id,
    async_get_renogy_device_info,
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Renogy Charge Controller based on a config entry."""
    coordinator: RenogyDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    entities = []
    for switch in SWITCH_TYPES:
        entity_desc = RenogyEntityDescription(
            key=switch.key,
            device_class=DEVICE_CLASS_SWITCH,
            device_info=await async_get_renogy_device_info(entry),
            entity_registry_enabled_default=True,
            name=switch.name,
            icon=switch.icon,
        )
        entities.append(RenogySwitch(coordinator, entity_desc))
    async_add_entities(entities, True)


class RenogySwitch(RenogyDeviceEntity, SwitchEntity):
    """Representation of a switch entity for the Renogy Rover Charge Controller."""

    def __init__(
        self,
        coordinator: RenogyDataUpdateCoordinator,
        description: RenogyEntityDescription,
    ) -> None:
        """Initialize a Renogy Switch."""
        super().__init__(coordinator=coordinator, description=description)

    @property
    def is_on(self) -> bool:
        """Return the state of the entity."""
        return self.coordinator.data[self.entity_description.key]

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn on the entity."""
        await self.async_turn(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off the entity."""
        await self.async_turn(False)

    async def async_turn(self, value: bool) -> None:
        """Update the value of the entity."""
        command = SWITCH_TYPES[self.entity_description.key].command(value)
        await self.hass.async_add_executor_job(
            self.coordinator.device.set_parameter,
            self.coordinator.modbus,
            command,
            self.coordinator.data,
        )

    async def async_added_to_hass(self) -> None:
        """Register callbacks."""
        await super().async_added_to_hass()
        self.async_on_remove(
            self.hass.helpers.event.async_track_time_interval(
                self.async_update,
                self.coordinator.update_interval,
            ),
        )


async def async_update(self) -> None:
        """Update the entity data."""
        await self.coordinator.async_request_refresh()