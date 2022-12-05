from utils import read_input
from day_05_solution_01 import build_initial_crate_stacks

def move_crates(move_instructions, crate_stacks):
    for line in move_instructions:
        _, num_to_move, _, from_stack, _, to_stack = line.split()

        crates = crate_stacks[from_stack][-int(num_to_move):]
        crate_stacks[from_stack] = crate_stacks[from_stack][:-int(num_to_move)]
        crate_stacks[to_stack] += crates
    return crate_stacks


if __name__ == "__main__":
    data = read_input(5)
    databreak_index = data.index("\n")

    # Parse start config from move instructions
    start_config, move_instructions = data[:databreak_index], data[databreak_index + 1:]

    crate_stacks = build_initial_crate_stacks(start_config)

    crate_stacks = move_crates(move_instructions, crate_stacks)

    tops = [stack.pop() for k, stack in sorted(crate_stacks.items(), key=lambda x: x[0])]

    print("".join(tops))
