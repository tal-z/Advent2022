import os

BASE_DIR = str(os.path.dirname(__file__))


def read_input(number: int):
    number = str(number)
    filepath = BASE_DIR + f"/inputs/input_{number.zfill(2)}.txt"
    with open(filepath, 'r') as f:
        data = f.readlines()
    return data
