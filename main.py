import pidkit
from cli import parse_args
from plants import PLANTS
from log import make_run_dir, log, chart

def build_plant(plant_class):
    parameters = {}
    for (parameter, spec) in plant_class.PARAMS.items():
        choice = input(f"{spec['prompt']}: " )
        if not choice:
            parameters[parameter] = spec.get("default")
        else:
            parameters[parameter] = spec["type"](choice)

    instance = plant_class(**parameters)
    return instance

def build_pid():
    setpoint = float(input("Setpoint: "))
    kp = float(input("kp: "))
    ki = float(input("ki: "))
    kd = float(input("kd: "))
    min_output = float(input("min_output: "))
    max_output = float(input("max_output: "))
    return pidkit.PID(kp, ki, kd, setpoint, output_limits=(min_output, max_output)), setpoint

def run():
    args = parse_args()
    plant = build_plant(PLANTS[args.plant])
    pid, setpoint = build_pid()

    t = 0
    run_log = []
    for i in range(args.steps):
        pv = plant.get_state()
        control_output = pid.compute(pv, args.timestep)
        error = setpoint - pv
        plant.step(control_output, args.timestep)

        step = (round(t, 5), setpoint, pv, error, control_output)
        run_log.append(step)

        t += args.timestep

    run_dir = make_run_dir(args.plant)
    log(run_log, run_dir)
    chart(run_log, run_dir)
    print("Simulation Complete!")

if __name__ == "__main__":
    run()