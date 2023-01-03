from utils import read_input

data = read_input(12)

grid = [list(s.strip()) for s in data]

rows = len(grid)
cols = len(grid[0])


def height(coord):
    row, col = coord
    letter = grid[row][col]

    if letter == "S":
        return 0
    if letter == "E":
        return 25
    return ord(letter) - 97


def find_start_and_end(g):
    start = None
    end = None

    for row in range(rows):
        for col in range(cols):
            if g[row][col] == "S":
                start = row, col
            if g[row][col] == "E":
                end = row, col
            if start and end:
                break

    return start, end


def valid_neighbors(current_coord):
    """
    Checks up, down, left, and right to determine whether those neighbors are reachable.
    A neighbor is reachable if their height is <= (1 + height of current coordinate).
    """
    row, col = current_coord

    up_coord = row - 1, col
    down_coord = row + 1, col
    right_coord = row, col - 1
    left_coord = row, col + 1

    valid_neighbors = []

    # Look up
    if (row > 0) and (height(up_coord) <= 1 + height(current_coord)):
        valid_neighbors.append(up_coord)

    # Look down
    if (row < rows - 1) and (height(down_coord) <= 1 + height(current_coord)):
        valid_neighbors.append(down_coord)

    # Look right
    if (col > 0) and (height(right_coord) <= 1 + height(current_coord)):
        valid_neighbors.append(right_coord)

    # Look left
    if (col < cols - 1) and (height(left_coord) <= 1 + height(current_coord)):
        valid_neighbors.append(left_coord)

    return valid_neighbors


if __name__ == "__main__":
    """
    1. Find starting and ending points.
    2. Find all reachable neighbors, and add them to a list of neighbors to visit.
    3. Add 1 to step count.
    4. For each neighbor in the list to visit, 
        check if it is the end. If it is the end, return step count.
    5. For each neighbor in the list to visit, find all reachable neighbors 
        and add them to a new list to visit.
    6. Repeat steps 3-5 until the end is reached.
    """



    start, end = find_start_and_end(grid)
    print(start, end)

    visited = set()

    steps = 0

    neighbors = {start}

    while neighbors:
        print(steps)
        new_neighbors = set()
        for neighbor in neighbors:
            if neighbor == end:
                print("END REACHED:", steps)
                break
            new_neighbors.update(set(valid_neighbors(neighbor)))
            visited.add(neighbor)
            new_neighbors -= visited

        neighbors = new_neighbors
        steps += 1

