from utils import read_input

data = read_input(8)

tree_matrix = [
    list(map(int, list(row.strip()))) for row in data
]

ROW_LENGTH = COLUMN_LENGTH = len(tree_matrix)

visible_set = set()


def is_max_from_left(x, y):
    value_to_check = tree_matrix[x][y]
    row = tree_matrix[x][:y+1]
    return [val for val in row if val >= value_to_check] == [value_to_check]


def is_max_from_right(x, y):
    value_to_check = tree_matrix[x][y]
    row = tree_matrix[x][y:]
    return [val for val in row if val >= value_to_check] == [value_to_check]


def is_max_from_top(x, y):
    value_to_check = tree_matrix[x][y]
    col = [row[y] for row in tree_matrix[:x+1]]
    return [val for val in col if val >= value_to_check] == [value_to_check]


def is_max_from_bottom(x, y):
    value_to_check = tree_matrix[x][y]
    col = [row[y] for row in tree_matrix[x:]]
    return [val for val in col if val >= value_to_check] == [value_to_check]


if __name__ == "__main__":

    for x in range(ROW_LENGTH):
        for y in range(COLUMN_LENGTH):

            # Add edges to visible set
            if x == 0 or y == 0:
                visible_set.add((x,y))
            elif x == ROW_LENGTH-1 or y == COLUMN_LENGTH-1:
                visible_set.add((x,y))

            # Add interiors if they are not the greatest value in their slice of a given list
            if is_max_from_left(x,y):
                visible_set.add((x,y))
            if is_max_from_right(x,y):
                visible_set.add((x,y))
            elif is_max_from_top(x,y):
                visible_set.add((x,y))
            elif is_max_from_bottom(x,y):
                visible_set.add((x,y))

print(len(sorted(visible_set)))



