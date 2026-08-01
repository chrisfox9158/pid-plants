from datetime import datetime
from pathlib import Path
import csv

def make_run_dir(plant_name):
    timestamp = datetime.now().strftime("%Y-%m-%d__%H.%M.%S")
    run_dir = Path("runs") / f"{timestamp}__{plant_name}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir

def log(rows, run_dir):
    filepath = run_dir / "log.csv"
    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["time", "setpoint", "pv", "error", "control_output"])
        writer.writerows(rows)