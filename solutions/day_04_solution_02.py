from utils import read_input
from day_04_solution_01 import parse_ranges

def ranges_overlap(r1, r2):
    overlap = set(r1).intersection(set(r2))
    if overlap:
        return True
    return False


data = read_input(4)

overlapping = 0
for line in data:
    range1_boundaries, range2_boundaries = parse_ranges(line)
    range_1 = range(range1_boundaries[0], range1_boundaries[1]+1)
    range_2 = range(range2_boundaries[0], range2_boundaries[1]+1)

    overlapping += ranges_overlap(range_1, range_2)

print(overlapping)
