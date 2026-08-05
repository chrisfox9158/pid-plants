# Thermostat (Delayed) Plant
Same first-order thermal lag as the standard `thermostat` plant, with an added dead time: control output $u$ does not affect the plant until $\theta$ seconds after it is applied.

## Model equation
$$
\frac{dT}{dt} = \frac{-(T_{current} - T_{ambient}) + K \cdot u_{delayed}}{\tau}
$$

Identical to the standard thermostat equation, except $u_{delayed}$ is the control output from $\theta$ seconds ago rather than current.

- **$\theta$** (`theta`) — dead time, in seconds, before control effects.
- All other terms match the standard [Thermostat Plant](thermostat_README.md).

## Parameters
| Parameter | Meaning | Default |
|---|---|---|
| `control_scale` | $K$, steady-state °C per unit of control output | `1.0` |
| `response_scale` | $\tau$, time constant in seconds | `60.0` |
| `t_ambient` | Ambient (drift goal) room temperature (°C) | `21.0` |
| `t_initial` | Starting room temperature (°C) | `t_ambient` |
| `dt` | Timestep — **must** match the run's `--timestep` exactly | `1` |
| `theta` | $\theta$, dead time in seconds | `5.0` |

## Configuration notes
- **`dt` must match `--timestep` exactly.** The plant's delay buffer is sized at construction using `theta / dt`; a mismatch between the two raises a clear error at `step()` time.
- **A larger $\theta$ relative to $\tau$** makes the plant meaningfully harder to control. Dead-time-dominant systems (roughly $\theta/\tau \geq 0.3$) can be checked against classical tuning formulas like Cohen-Coon; see [pidkit's autotuning docs](https://github.com/chrisfox9158/pidkit/blob/main/docs/autotuning.md) for a worked comparison.