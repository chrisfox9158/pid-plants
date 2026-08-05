import pidkit
from cli import parse_args
from plants import PLANTS
from log import make_run_dir, log, chart

def build_factory(plant_class):
    parameters = {}
    for (parameter, spec) in plant_class.PARAMS.items():
        choice = input(f"{spec['prompt']}: " )
        if not choice:
            parameters[parameter] = spec.get("default")
        else:
            parameters[parameter] = spec["type"](choice)

    plant_factory = lambda: plant_class(**parameters)
    return plant_factory

def build_tune_config():
    setpoint = float(input("Setpoint: "))
    min_output = float(input("min_output: "))
    max_output = float(input("max_output: "))
    output_limits = (min_output, max_output)

    aggression = float(input("Aggression: "))
    base_effort_weight = float(input("Base effort weight: "))
    return setpoint, output_limits, aggression, base_effort_weight

def run():
    args = parse_args()
    factory = build_factory(PLANTS[args.plant])
    setpoint, output_limits, aggression, base_effort_weight = build_tune_config()

    result = pidkit.autotune_sim(plant_factory=factory, setpoint=setpoint, dt=args.timestep, steps=args.steps, output_limits=output_limits,
                                aggression=aggression, base_effort_weight=base_effort_weight)

    setpoint_list = [setpoint] * len(result.times)
    run_log = list(zip(result.times, setpoint_list, result.pv_values, result.errors, result.control_outputs))

    run_dir = make_run_dir(args.plant)
    log(run_log, run_dir)
    chart(run_log, run_dir)
    print("Simulation Complete!\n")
    print(f"Gains found!:")
    print(f"kp: {result.kp}")
    print(f"ki: {result.ki}")
    print(f"kd: {result.kd}")

if __name__ == "__main__":
    run()