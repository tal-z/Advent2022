from utils import read_input
from day_06_solution_01 import no_repeats


if __name__ == "__main__":

    data = read_input(6)[0]

    for i in range(14, len(data)+1):
        leading_fourteen = data[i-14:i]
        if no_repeats(leading_fourteen):
            print(i)
            break
