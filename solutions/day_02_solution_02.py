from utils import read_input
from day_02_solution_01 import score_round

move_values = {
    "A": 1,
    "B": 2,
    "C": 3,
}

win_moves = {
    "A": "B",
    "B": "C",
    "C": "A",
}

draw_moves = {
    "A": "A",
    "B": "B",
    "C": "C",
}

lose_moves = {
    "A": "C",
    "B": "A",
    "C": "B",
}

needed_moves = {
    "X": lose_moves,
    "Y": draw_moves,
    "Z": win_moves,
}


def needed_move(p1_move, win_lose_draw_val):
    return needed_moves[win_lose_draw_val][p1_move]


if __name__ == "__main__":

    data = read_input(2)

    total_score = 0
    for moves in data:
        p1_move, win_lose_draw_val = moves.strip().split()
        p2_move = needed_move(p1_move, win_lose_draw_val)

        p1_value = move_values[p1_move]
        p2_value = move_values[p2_move]

        total_score += score_round(p1_value, p2_value)

    print(total_score)
