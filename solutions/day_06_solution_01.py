from utils import read_input


def no_repeats(string):
    return len(set(string)) == len(string)


if __name__ == "__main__":

    data = read_input(6)[0]

    for i in range(4, len(data)+1):
        leading_four = data[i-4:i]
        if no_repeats(leading_four):
            print(i)
            break
