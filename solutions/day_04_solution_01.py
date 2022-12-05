from typing import Tuple
from utils import read_input

data = read_input(4)

def parse_ranges(dataline: str) -> Tuple:
    range_1, range_2 = dataline.split(",")
    range_1 = tuple(int(num) for num in range_1.split("-"))
    range_2 = tuple(int(num) for num in range_2.strip().split("-"))
    return range_1, range_2


def range_contains_range(r1, r2) -> bool:
    if r1[0] >= r2[0] and r1[1] <= r2[1]:
        return True
    if r2[0] >= r1[0] and r2[1] <= r1[1]:
        return True
    return False


if __name__ == "__main__":
    fully_contained = 0
    for line in data:
        range_boundaries = parse_ranges(line)
        fully_contained += range_contains_range(*range_boundaries)
    print(fully_contained)


