with open("day11/11input.txt", "r") as file:
    file_contents = file.readlines()


class Monkey():

    def __init__(self, id, starting_items, operation, test, true_target, false_target):
        self.id = id
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.true_target = true_target
        self.false_target = false_target

    def pass_item_to(self, monkey):

        item = self._items.pop(0)
        monkey.receive_item(item)


current = 0
monkeys = [{} for _ in range(8)]
for line in file_contents:
    if line.startswith("M"):
        monkeys[current]["id"] = line.split()[1]

    elif line.startswith("  S"):
        monkeys[current]["list"] = line.split()[2:]

    elif line.startswith("  O"):
        operation = line.split()[3:]
        monkeys[current]["operation"] = operation
    elif line.startswith("  T"):
        divisible_by = line.split()[-1]
        monkeys[current]["divisible"] = divisible_by
    elif line.startswith("    If t"):
        throw_to = line.split()[-1]
        monkeys[current]["throw_true"] = throw_to
    elif line.startswith("    If f"):
        throw_to = line.split()[-1]
        monkeys[current]["throw_false"] = throw_to
        current += 1

print(monkeys)

for i, monkey in enumerate(monkeys):
    
    for item in monkey["list"]:
        level = item[:2]
        operation = +
        if monkey["operation"] == "*": operation = *

        level
        

