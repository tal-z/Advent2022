import argparse, os


# Gather our code in a main() function
def main(args):
    daynum = str(args.daynum).zfill(2)
    os.chdir("inputs")
    with open(f"input_{daynum}.txt", "w"):
        pass

    os.chdir("../solutions")
    with open(f"day_{daynum}_solution_01.py", "w"):
        pass
    with open(f"day_{daynum}_solution_02.py", "w"):
        pass




# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Creates files for a new day of Advent of Code."
    )

    parser.add_argument(
        "--daynum",
        help="pass ARG to the program",
    )

    args = parser.parse_args()


    main(args)