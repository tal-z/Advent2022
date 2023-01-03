from utils import read_input


def addx(x, v, cycle_count, cycle_values):
    cycle_count += 1
    cycle_values[cycle_count] = x
    cycle_count += 1
    cycle_values[cycle_count] = x + v
    return cycle_values[cycle_count], cycle_count, cycle_values

def noop(x, cycle_count, cycle_values):
    cycle_count += 1
    cycle_values[cycle_count] = x
    return cycle_values[cycle_count], cycle_count, cycle_values


def signal_strength(cycle_values):
    total = 0
    cycle = 20

    while cycle <= 220:
        total += cycle_values[cycle-1] * cycle
        cycle += 40

    return total



def process_instructions(data):
    cycle_count = 0
    cycle_values = {}
    x = 1

    for line in data:
        line = line.strip().split()
        instruction = line[0]

        if instruction == "addx":
            v = int(line[1])
            x, cycle_count, cycle_values = addx(x, v, cycle_count, cycle_values)
        elif instruction == "noop":
            x, cycle_count, cycle_values = noop(x, cycle_count, cycle_values)

    return cycle_values


if __name__ == "__main__":

    data = read_input(10)

    cycle_values = process_instructions(data)

    print(signal_strength(cycle_values))



