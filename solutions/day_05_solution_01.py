from utils import read_input


def parse_start_config_row(row):
    parsed_row = []
    curr = ""
    for char in row:
        curr += char
        if len(curr) == 4:
            parsed_row.append(curr.strip(" \n[]"))
            curr = ""
    parsed_row.append(curr.strip())

    return parsed_row


def build_initial_crate_stacks(start_config):
    # build a dictionary of empty stacks
    # based on the last row of start config.
    crate_stacks = {
        k: []
        for k in start_config.pop().strip().split(" ")
        if k
    }

    # iterate through start config and populate stacks in dict.
    # Add crates to the front of the stack, since we are iterating backwards.
    for row in start_config:
        parsed_row = parse_start_config_row(row)
        stack_count = 1
        for crate in parsed_row:
            if crate:
                crate_stacks[str(stack_count)].insert(0, crate)
            stack_count += 1
    return crate_stacks


def move_crates(move_instructions, crate_stacks):
    for line in move_instructions:
        _, num_to_move, _, from_stack, _, to_stack = line.split()

        for _ in range(int(num_to_move)):
            crate_stacks[to_stack].append(crate_stacks[from_stack].pop())

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
