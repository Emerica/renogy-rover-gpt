import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_MAC, CONF_NAME
from homeassistant.core import callback

from .const import DOMAIN
from .renogy_bt1 import BTOneApp

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema(
    {vol.Required(CONF_MAC): str, vol.Required(CONF_NAME, default="Renogy BT-1"): str}
)

async def validate_input(hass, data):
    """Validate the user input allows us to connect."""
    bt1 = BTOneApp(data[CONF_MAC])
    try:
        await bt1.connect()
    except Exception as exception:
        raise CannotConnect from exception
    finally:
        await bt1.disconnect()

class CannotConnect(Exception):
    """Error to indicate we cannot connect."""

    pass

@config_entries.HANDLERS.register(DOMAIN)
class RenogyBT1FlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a Renogy BT-1 config flow."""

    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            try:
                await validate_input(self.hass, user_input)
                return self.async_create_entry(
                    title=user_input[CONF_NAME], data=user_input
                )
            except CannotConnect:
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return RenogyBT1OptionsFlowHandler(config_entry)

class RenogyBT1OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle a Renogy BT-1 options flow."""

    def __init__(self, config_entry):
        """Initialize the options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle user input."""
        if user_input is not None:
            self.hass.config_entries.async_update_entry(
                self.config_entry, data=user_input
            )
            return self.async_create_entry(title="", data=None)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME, default=self.config_entry.data[CONF_NAME]
                    ): str,
                    vol.Required(
                        CONF_MAC, default=self.config_entry.data[CONF_MAC]
                    ): str,
                }
            ),
        )
