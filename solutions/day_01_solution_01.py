from collections import defaultdict
from utils import read_input

data = read_input(1)

elf_calories = defaultdict(lambda: 0)
elf_num = 1

for row in data:
    if row == "\n":
        elf_num += 1
        continue
    cals = int(row.strip())
    elf_calories[elf_num] += cals

answer = max(elf_calories.values())
print(answer)
