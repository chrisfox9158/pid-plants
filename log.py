from datetime import datetime
from pathlib import Path
import csv
import matplotlib.pyplot as plt

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

def chart(rows, run_dir):
    t_values = [row[0] for row in rows]
    setpoint_value = [row[1] for row in rows][0]
    pv_values = [row[2] for row in rows]
    error_values = [row[3] for row in rows]
    control_values = [row[4] for row in rows]

    # Response curve chart
    fig1, ax1 = plt.subplots()
    ax1.plot(t_values, pv_values, label="Process Variable")
    ax1.axhline(y=setpoint_value, color="gray", linestyle="--", label="Setpoint")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Value")
    ax1.set_title("Response Curve")
    ax1.legend()
    fig1.savefig(run_dir / "response.png")
    plt.close(fig1)

    # Error and control chart
    fig2, (ax2, ax3) = plt.subplots(2, 1, sharex=True)
    ax2.plot(t_values, error_values, color="tab:red")
    ax2.set_ylabel("Error")
    ax3.plot(t_values, control_values, color="tab:blue")
    ax3.set_ylabel("Control Output")
    ax3.set_xlabel("Time")
    fig2.suptitle("Error and Control Output")
    fig2.savefig(run_dir / "error_control.png")
    plt.close(fig2)