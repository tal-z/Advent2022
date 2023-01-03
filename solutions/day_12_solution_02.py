from utils import read_input
from day_12_solution_01 import valid_neighbors

def find_starts_and_end(g):
    starts = set()
    end = None

    for row in range(rows):
        for col in range(cols):
            if g[row][col] in {"a", "S"}:
                starts.add((row, col))
            if g[row][col] == "E":
                end = row, col


    return starts, end

if __name__ == "__main__":

    data = read_input(12)

    grid = [list(s.strip()) for s in data]
    # print(*grid, sep="\n")

    rows = len(grid)
    cols = len(grid[0])

    starts, end = find_starts_and_end(grid)
    print(starts, end)

    visited = set()

    steps = 0

    neighbors = starts

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

