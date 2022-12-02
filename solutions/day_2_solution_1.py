from utils import read_input


move_values = {
    # Player 1
    "A": 1,
    "B": 2,
    "C": 3,
    # Player 2
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def score_round(p1_value, p2_value):
    """
    The score for a single round is the score for the shape you selected
    (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round
    (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    outcome = p2_value-p1_value
    if outcome in {1, -2}:
        # win case
        return p2_value + 6
    if not outcome:
        # tie case
        return p2_value + 3
    # loss case
    return p2_value

if __name__ == "__main__":

    data = read_input(2)

    total_score = 0
    for moves in data:
        p1_move, p2_move = moves.strip().split()

        p1_value = move_values[p1_move]
        p2_value = move_values[p2_move]

        total_score += score_round(p1_value, p2_value)

    print(total_score)
