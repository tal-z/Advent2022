from utils import read_input

class Monkey():

    def __init__(self, id):
        # list of integers representing items as worry levels
        self.id = id
        self.operation = None
        self.starting_items = None
        self.test_divisor = None
        self.if_true = None
        self.if_false = None
        self.inspection_count = 0

    def __str__(self):
        return f"Monkey {self.id}: {str(self.__dict__)}"

    def inspect_next_item(self, mod_val):
        self.inspection_count += 1
        item_worry_level = self.starting_items.pop(0)
        new_worry_level = self.execute_operation(item_worry_level) % mod_val
        if not new_worry_level % self.test_divisor:
            self.throw_to_monkey(new_worry_level, self.if_true)
        else:
            self.throw_to_monkey(new_worry_level, self.if_false)

    def throw_to_monkey(self, item, new_monkey_id):
        receiving_monkey = monkies[new_monkey_id]
        receiving_monkey.starting_items.append(item)


    def execute_operation(self, old):
        operation = self.operation.replace("old", str(old))
        return eval(operation)


def monkey_business(monkies):
    m1, m2 = sorted([m.inspection_count for m in monkies.values()], reverse=True)[:2]
    return m1 * m2

if __name__ == "__main__":

    data = read_input(11)

    monkies = {}

    curr_monkey = None

    for line in data:
        line = line.strip()
        if line.startswith("Monkey"):
            curr_monkey = line.split()[1][:-1]
            monkies[curr_monkey] = Monkey(id=curr_monkey)
        elif line.startswith("Starting items"):
            items = list(map(int, line.split(": ")[1].split(",")))
            monkies[curr_monkey].starting_items = items
        elif line.startswith("Operation"):
            op = line.split(": ")[1].split(" = ")[1]
            monkies[curr_monkey].operation = op
        elif line.startswith("Test"):
            test_divisor = int(line.split(": ")[1].split()[-1])
            monkies[curr_monkey].test_divisor = test_divisor
        elif line.startswith("If true"):
            if_true = line.split(": ")[1].split()[-1]
            monkies[curr_monkey].if_true = if_true
        elif line.startswith("If false"):
            if_false = line.split(": ")[1].split()[-1]
            monkies[curr_monkey].if_false = if_false

    from math import prod
    SUPERMODULO = prod([m.test_divisor for m in monkies.values()])

    for _ in range(10000):
        #print("ROUND", _)
        for id, monkey in monkies.items():
            #print("MONKEY", id)
            while monkey.starting_items:
                #print(len(monkey.starting_items))
                monkey.inspect_next_item(SUPERMODULO)

    #for _, monkey in monkies.items():
     #   print(monkey)
    print(monkey_business(monkies))


