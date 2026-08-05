from .thermostat.thermostat import Thermostat
from .thermostat_delayed.thermostat_delayed import ThermostatDelayed
from .cart_velocity.cart_velocity import CartVelocity

PLANTS = {
    "thermostat": Thermostat,
    "thermostat_delayed": ThermostatDelayed,
    "cart_velocity": CartVelocity
}