# Thermostat Plant
Simulates a single-zone room heater as a first-order thermal lag system. A heater (control output $u$) pushes room temperature away from ambient; thermal mass causes response lag behind the control signal rather than snapping instantly.

## Model equation
$$
\frac{dT}{dt} = \frac{-(T_{current} - T_{ambient}) + K * u}{\tau}
$$

- **$T_{current}$** — current room temperature (state)
- **$T_{ambient}$** — the temperature the room drifts toward with no heating ($u = 0$)
- **$K$** (`control_scale`) — steady-state gain. If $u$ is held constant forever, the room settles at $T_{ambient} + K * u$.
- **$\tau$** (`response_scale`) — time constant, in seconds. After $\tau$ seconds of a step change in $u$, the room has covered ~63% of the distance to the new value; after $5\tau$ seconds, effectively settled (>99%).

## Parameters
| Parameter | Meaning | Default |
|---|---|---|
| `control_scale` | $K$, steady-state °C per unit of control output | `1.0` |
| `response_scale` | $\tau$, time constant in seconds | `60.0` |
| `t_ambient` | Ambient (drift goal) room temperature (°C) | `21.0` |
| `t_initial` | Starting room temperature (°C) | `t_ambient` |

## Configuration Notes
- **`response_scale`** determines how long a run needs to be to see the plant settle. A user should size `--steps * --timestep` to at least $5\tau$.
- **`control_scale`** should be sized relative to your `output_limits` and target temperature gap. If `output_limits` caps $u$ tightly, too small a `control_scale` means the heater can never plausibly reach setpoint.