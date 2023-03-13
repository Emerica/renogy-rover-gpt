import logging

from homeassistant.helpers.entity import Entity
from .const import DOMAIN, SENSOR_TYPES

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    bt1 = hass.data[DOMAIN][config_entry.entry_id]
    entities = []

    for sensor in SENSOR_TYPES:
        entities.append(RoverSensor(bt1, sensor))

    async_add_entities(entities, True)

class RoverSensor(Entity):

    def __init__(self, bt1, sensor):
        self.bt1 = bt1
        self._name = f"{bt1.name} {sensor.name}"
        self._unique_id = f"{bt1.unique_id}_{sensor.key}"
        self._state = None
        self.sensor = sensor

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self.sensor.unit

    @property
    def icon(self):
        return self.sensor.icon

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.bt1.unique_id)},
            "name": self.bt1.name,
            "manufacturer": "Renogy"
        }

    async def async_update(self):
        data = await self.hass.async_add_executor_job(self.bt1.read)
        if self.sensor.key not in data:
            _LOGGER.warning("Sensor key %s not found in data", self.sensor.key)
            return
        self._state = data[self.sensor.key]
