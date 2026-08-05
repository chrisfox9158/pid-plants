# pid-plants
Simulated plant test-bed for validating [pidkit](https://github.com/chrisfox9158/pidkit) against a range of dynamic systems, and for exploring pidkit's autotuning capabilities against real plant behavior.

## Plants
- `thermostat` — first-order thermal lag.
- `cart_velocity` — first-order velocity with drag.
- `thermostat_delayed` — first-order thermal lag with dead-time.

## Usage
### Manual PID trial:
```bash
uv run main.py --plant thermostat --steps 600 --timestep 1
```

### Autotuned trial:
```bash
uv run tune.py --plant thermostat --steps 600 --timestep 1
```

Both prompt for plant-specific parameters and produce a CSV log and response-curve chart under `runs/<timestamp>_<plant>/`.