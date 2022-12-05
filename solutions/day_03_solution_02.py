from utils import read_input
from day_03_solution_01 import score_overlap


def find_badge(badge_group):
    overlap = set(badge_group.pop())
    for sack in badge_group:
        overlap = overlap.intersection(set(sack))
    return overlap


if __name__ == "__main__":

    rucksacks = read_input(3)

    badge_group = []
    priority_sum = 0

    for sack in rucksacks:
        badge_group.append(sack.strip())
        if len(badge_group) == 3:
            badge = find_badge(badge_group)
            priority_sum += score_overlap(badge)
            badge_group = []

    print(priority_sum)