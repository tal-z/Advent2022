from utils import read_input
from collections import defaultdict

def add_size_to_directory_and_all_parents(size, current_directory, directories):
    path = "/"
    for d in current_directory:
        path = path + d + "/"
        directories[path] += size

def build_directories(data):

    directories = defaultdict(lambda: 0)
    current_directory = []

    for line in data:
        line = line.strip()

        if line.startswith("$ cd"):
            if line[5:] == "..":
                current_directory.pop()
            else:
                current_directory.append(line[5:])

        elif line.startswith("$ ls"):
            pass

        elif line.startswith("dir"):
            pass

        else:
            size = int(line.split()[0])

            add_size_to_directory_and_all_parents(size, current_directory, directories)

    return directories


if __name__ == "__main__":

    data = read_input(7)

    directories = build_directories(data)

    ans = sum([v for k, v in directories.items() if v <= 100000])

    print(ans)