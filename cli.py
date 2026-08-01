import argparse
from plants import PLANTS

def parse_args():
    parser = argparse.ArgumentParser(description="Plant testbed for pidkit validation against dynamic simulations")
    parser.add_argument("--plant", choices=PLANTS.keys(), help="Plant simulation model")
    return parser.parse_args()