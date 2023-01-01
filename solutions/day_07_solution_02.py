from utils import read_input
from day_07_solution_01 import build_directories, add_size_to_directory_and_all_parents


AVAILABLE_SPACE = 70000000
NEEDED_SAPCE = 30000000

if __name__ == "__main__":

    data = read_input(7)

    directories = build_directories(data)

    unused_space = AVAILABLE_SPACE - directories["///"]

    additional_space_needed = NEEDED_SAPCE - unused_space

    min_directory_size = directories["///"]
    for directory, size in directories.items():
        min_directory_size = min_directory_size if size < additional_space_needed else min(min_directory_size, size)

    print(min_directory_size)