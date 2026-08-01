import pidkit
from cli import parse_args
from plants import PLANTS

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
    max_output = float(input("max_output: "))
    min_output = float(input("min_output: "))
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
        t += args.timestep

        step = (t, setpoint, pv, error, control_output)
        run_log.append(step)

    print(run_log)

if __name__ == "__main__":
    run()