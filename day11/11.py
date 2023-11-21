with open("day11/11input.txt", "r") as file:
    file_contents = file.readlines()


def parse_monkeys():

    current = 0
    monkeys = [{} for _ in range(8)]

    for line in file_contents:
        monkeys[current]["times_inspected"] = 0

        if "Monkey" in line:
            monkeys[current]["id"] = line.split()[1][0]
        elif "Starting" in line:
            monkeys[current]["items"] = []
            for item in line.split()[2:]:
                monkeys[current]["items"].append(int(item[0:2]))
            monkeys[current]["thrown_items"] = monkeys[current]["items"]
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

    return monkeys


"""
Example:

0, 10, 20, 30, etc % 10 = 0

mod 10 is divisible by 2 and 5


13 * 11 = 143

if you apply % 143 to a number and is equal to 0, then is divisible by both of them.

in this case, applying a modulo that is divisible by all tests guarantees a way to check if the number is divisible by any of them, just as if the number never changed.

"""


def get_most_active_monkeys(monkeys):
    most_active_monkeys = [0, 0]
    for monkey in monkeys:

        for i in range(2):
            if monkey["times_inspected"] > most_active_monkeys[i]:
                most_active_monkeys.insert(i, monkey["times_inspected"])
                most_active_monkeys = most_active_monkeys[:2]
                break
    return (most_active_monkeys[0] * most_active_monkeys[1])


def monkey_bussiness(monkeys, iteration, operation):
    for _ in range(iteration):
        for monkey in monkeys:

            monkey["items"] = monkey["thrown_items"]
            monkey["thrown_items"] = []
            for item in monkey["items"]:
                worry_level = item

                second_number = item if monkey["operation"][2] == "old" else int(
                    monkey["operation"][2])

                worry_level = item * \
                    second_number if monkey["operation"][1] == "*" else item + \
                    second_number

                worry_level = operation(worry_level)

                if worry_level % int(monkey["divisible"]) == 0:
                    monkey_to_throw_to = int(monkey["throw_true"])

                else:
                    monkey_to_throw_to = int(monkey["throw_false"])

                monkeys[monkey_to_throw_to]["thrown_items"].append(
                    worry_level)
                monkey["times_inspected"] += 1

    return get_most_active_monkeys(monkeys)


def monkey_bussiness_with_module(monkeys):
    modulo = 1
    for monkey in monkeys:
        modulo = modulo * int(monkey["divisible"])

    return monkey_bussiness(monkeys, 10000, lambda x: x % modulo)


print(monkey_bussiness(parse_monkeys(), 20, operation=lambda x: x // 3))
print(monkey_bussiness_with_module(parse_monkeys()))
