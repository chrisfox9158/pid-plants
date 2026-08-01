import argparse
from plants import PLANTS

def parse_args():
    parser = argparse.ArgumentParser(description="Plant testbed for pidkit validation against dynamic simulations")
    parser.add_argument("--plant", choices=PLANTS.keys(), required=True, help="Plant simulation model")
    parser.add_argument("--steps", type=int, default=100, help="Steps run for PID loop")
    parser.add_argument("--timestep", type=float, default=0.1, help="dt timestep for PID loop")
    return parser.parse_args()