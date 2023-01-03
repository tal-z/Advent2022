from utils import read_input


def move_tail(head, tail):
    x_diff = head[0] - tail[0]  # row
    y_diff = head[1] - tail[1]  # col

    if -1 <= x_diff <= 1 and -1<= y_diff <= 1:
        return tail

    if x_diff >= 2:
        new_x = tail[0] + x_diff - 1
    elif x_diff <= -2:
        new_x = tail[0] + x_diff + 1
    else:
        new_x = tail[0] + x_diff

    if y_diff >= 2:
        new_y = tail[1] + y_diff - 1
    elif y_diff <= -2:
        new_y = tail[1] + y_diff + 1
    else:
        new_y = tail[1] + y_diff

    return new_x, new_y


if __name__ == "__main__":

    data = read_input(9)

    head = 0, 0
    tail = 0, 0

    tail_visited = {tail}

    for line in data:
        direction, count = line.split()
        # Simulate head movements
        for _ in range(int(count)):
            if direction == "R":
                head = head[0], head[1] + 1
            elif direction == "L":
                head = head[0], head[1] - 1
            elif direction == "U":
                head = head[0] - 1, head[1]
            elif direction == "D":
                head = head[0] + 1, head[1]

            # Follow with tail movement
            tail = move_tail(head, tail)
            tail_visited.add(tail)

    print(len(tail_visited))