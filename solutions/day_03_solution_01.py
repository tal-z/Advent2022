from utils import read_input


def split_sack(sack):
    sack = sack.strip()
    mid = len(sack)//2
    return set(sack[:mid]), set(sack[mid:])


def score_overlap(overlap):
    total = 0
    for char in overlap:
        if char.lower() == char:
            total += ord(char)-96
        else:
            total += ord(char.lower())-70
    return total


if __name__ == "__main__":
    rucksacks = read_input(3)

    priority_sum = 0
    for sack in rucksacks:
        compartment_1, compartment_2 = split_sack(sack)
        overlap = compartment_1.intersection(compartment_2)
        priority_sum += score_overlap(overlap)

    print(priority_sum)

