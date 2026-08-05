# Cart Velocity Plant
Simulates a cart's velocity under an applied force, with optional linear drag. Control output $u$ acts as an applied force; drag opposes motion proportionally to current velocity.

## Model equation
$$
\frac{dv}{dt} = \frac{u - b \cdot v_{current}}{m}
$$

- **$v_{current}$** — current velocity (state)
- **$m$** (`mass`) — inertia. Larger $m$ means the same force $u$ produces less acceleration.
- **$b$** (`opposing_force`) — drag/friction coefficient. With $b = 0$, the plant is a pure integrator with no natural damping at all.

## Parameters
| Parameter | Meaning | Default |
|---|---|---|
| `mass` | $m$, inertia | `5.0` |
| `opposing_force` | $b$, drag/friction coefficient | `0.0` |
| `v_initial` | Starting velocity | `0.0` |

## Configuration notes
- **$b = 0$** removes all natural damping so that the plant relies entirely on the controller for stability.
- **`mass`** and **`opposing_force`** together set the plant's effective time constant ($m/b$, when $b > 0$). $5\tau$-style sizing logic, as seen in the thermostat plant, applies here.