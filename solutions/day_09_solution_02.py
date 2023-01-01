from utils import read_input
from collections import defaultdict

from day_09_solution_01 import move_tail


def move_rope(rope):
    for i in range(len(rope)-1):
        head, tail = rope[i:i+2]
        new_tail = move_tail(head, tail)
        rope[i+1] = new_tail
    return rope



if __name__ == "__main__":

    data = read_input(9)

    rope = [(0, 0) for _ in range(10)]

    tail_visited = {rope[-1]}

    for line in data:
        direction, count = line.split()
        # Simulate rope movements
        for _ in range(int(count)):
            head = rope.pop(0)

            if direction == "R":
                head = head[0], head[1] + 1
                rope = move_rope([head] + rope)
            elif direction == "L":
                head = head[0], head[1] - 1
                rope = move_rope([head] + rope)

            elif direction == "U":
                head = head[0] - 1, head[1]
                rope = move_rope([head] + rope)

            elif direction == "D":
                head = head[0] + 1, head[1]
                rope = move_rope([head] + rope)

            tail_visited.add(rope[-1])

    print(len(tail_visited))