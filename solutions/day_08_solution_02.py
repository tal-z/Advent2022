from utils import read_input

data = read_input(8)

tree_matrix = [
    list(map(int, list(row.strip()))) for row in data
]

ROW_LENGTH = COLUMN_LENGTH = len(tree_matrix)

visible_set = set()


def visible_from_left(x, y):
    current_tree = tree_matrix[x][y]
    num_visible = 0
    left = y-1
    while left >= 0:
        if tree_matrix[x][left] < current_tree:
            num_visible += 1
            left -= 1
        else:
            num_visible += 1
            break
    return num_visible


def visible_from_right(x, y):
    current_tree = tree_matrix[x][y]
    num_visible = 0
    right = y + 1
    while right < ROW_LENGTH:
        if tree_matrix[x][right] < current_tree:
            num_visible += 1
            right += 1
        else:
            num_visible += 1
            break
    return num_visible

def visible_from_top(x, y):
    current_tree = tree_matrix[x][y]
    num_visible = 0
    up = x - 1
    while up >= 0:
        if tree_matrix[up][y] < current_tree:
            num_visible += 1
            up -= 1
        else:
            num_visible += 1
            break
    return num_visible

def visible_from_bottom(x, y):
    current_tree = tree_matrix[x][y]
    num_visible = 0
    down = x + 1
    while down < COLUMN_LENGTH:
        if tree_matrix[down][y] < current_tree:
            num_visible += 1
            down += 1
        else:
            num_visible += 1
            break
    return num_visible

def scenic_score(x, y):
    left = visible_from_left(x,y)
    right = visible_from_right(x,y)
    top = visible_from_top(x, y)
    bottom = visible_from_bottom(x, y)
    return left * right * top * bottom

if __name__ == "__main__":

    max_scenic_score = 0
    for x in range(ROW_LENGTH):
        for y in range(COLUMN_LENGTH):
            max_scenic_score = max(max_scenic_score, scenic_score(x,y))

    print(max_scenic_score)


