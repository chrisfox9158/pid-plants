# pid-plants
Simulated plant test-bed for validating [pidkit](https://github.com/chrisfox9158/pidkit) against a range of dynamic systems, and for exploring pidkit's automatic gain-tuning capabilities against real plant behavior.

## Purpose
`pid-plants` exists to test `pidkit` under actual simuation conditions. This repository includes a small set of simulated physical systems, each implementing a minimal `step`/`get_state` contract, that `pidkit`'s `PID` class and `autotune_sim` function can be run against.

## Architecture
- **`cli.py`** — argparse layer. Defines `--plant`, `--steps`, `--timestep`, shared by the `main.py` and `tune.py` entry-points.
- **`main.py`** — manual PID trial. Prompts for plant parameters and PID gains; runs the control loop and logs/charts the results.
- **`tune.py`** — autotuned trial. Prompts for plant parameters and tuning options (`setpoint`, `output_limits`, `aggression`); calls `pidkit.autotune_sim` and logs/charts the resulting gains.
- **`log.py`** — CSV logging (`log()`) and matplotlib response-curve plotting (`chart()`); controls `runs/` directory creation.
- **`plants/`** — registry (`PLANTS` dict in `__init__.py`) mapping plant name to class. Each plant is self-contained: implements `step(u, dt)` and `get_state()`, declares its own `PARAMS` spec for prompt generation, and is entirely modular/self-contained.

## Plants
- [`thermostat`](plants/thermostat/README.md) — first-order thermal lag.
- [`cart_velocity`](plants/cart_velocity/README.md) — first-order velocity with drag.
- [`thermostat_delayed`](plants/thermostat_delayed/README.md) — first-order thermal lag with dead time.

Plant-specific usage instructions can be found in each plant's individual README, linked above.

## Setup
```bash
git clone https://github.com/chrisfox9158/pid-plants.git
cd pid-plants
uv sync
```

## Usage
Both systems prompt for plant-specific parameters and produce a CSV log alongside the error_control and response-curve charts under `runs/<timestamp>_<plant>/`.

### Manual PID Trial
```bash
uv run main.py --plant thermostat --steps 600 --timestep 1
```

### Autotuned PID Trial
```bash
uv run tune.py --plant thermostat --steps 600 --timestep 1
```

**Note on `aggression`:** this parameter requires hand-calibration for satisfactory results. For custom plant parameter sets, a user will likely need to test a few values between 0 and 1 (*recommended: 0.05, default 0.25, 0.4, 0.6, 0.95*) and reference the resulting chart for desired behavior (fast or slow approach; oscillation and overshoot behaviors). A full explanation can be found in [pidkit's autotuning docs](https://github.com/chrisfox9158/pidkit/blob/main/docs/autotuning.md).

## Repository Structure
```
plants/                     # Storage folder for simulated plant models
    thermostat/
        thermostat.py
        README.md
    cart_velocity/
        cart_velocity.py
        README.md
    thermostat_delayed/
        thermostat_delayed.py
        README.md
    __init__.py                 # PLANTS registry dict
cli.py                      # argparse for shared --plant/--steps/--timestep config
main.py                     # Manual PID trial orchestration
tune.py                     # Autotuned trial orchestration
log.py                      # CSV logging and matplotlib charting
runs/                       # Generated per-run output (gitignored)
```

## License
MIT License — see [LICENSE](LICENSE)