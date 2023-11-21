with open("day11/11input.txt", "r") as file:
    file_contents = file.readlines()


def monkeys():

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


def monkey_bussiness_with_module(monkeys):
    for _ in range(10000):
        modulo = 1
        for monkey in monkeys:
            modulo = modulo * int(monkey["divisible"])
        for monkey in monkeys:

            monkey["items"] = monkey["thrown_items"]
            monkey["thrown_items"] = []
            for item in monkey["items"]:
                worry_level = item
                second_number = monkey["operation"][2]

                if monkey["operation"][2] == "old":
                    second_number = item

                second_number = int(second_number)
                if monkey["operation"][1] == "*":
                    worry_level = worry_level * second_number
                else:
                    worry_level += second_number

                worry_level = worry_level % modulo
                if worry_level % int(monkey["divisible"]) == 0:
                    monkey_to_throw_to = int(monkey["throw_true"])
                    monkeys[monkey_to_throw_to]["thrown_items"].append(
                        worry_level)
                else:
                    monkey_to_throw_to = int(monkey["throw_false"])
                    monkeys[monkey_to_throw_to]["thrown_items"].append(
                        worry_level)
                monkey["times_inspected"] += 1

    highest_monkeys = [0, 0]
    for monkey in monkeys:

        for i in range(2):
            if monkey["times_inspected"] > highest_monkeys[i]:
                highest_monkeys.insert(i, monkey["times_inspected"])
                highest_monkeys = highest_monkeys[:2]

    return (highest_monkeys[0] * highest_monkeys[1])


def monkey_bussiness(monkeys):
    for _ in range(20):
        for monkey in monkeys:

            monkey["items"] = monkey["thrown_items"]
            monkey["thrown_items"] = []
            for item in monkey["items"]:
                worry_level = item
                second_number = monkey["operation"][2]

                if monkey["operation"][2] == "old":
                    second_number = item

                second_number = int(second_number)
                if monkey["operation"][1] == "*":
                    worry_level = worry_level * second_number
                else:
                    worry_level += second_number

                worry_level = worry_level // 3

                if worry_level % int(monkey["divisible"]) == 0:
                    monkey_to_throw_to = int(monkey["throw_true"])
                    monkeys[monkey_to_throw_to]["thrown_items"].append(
                        worry_level)
                else:
                    monkey_to_throw_to = int(monkey["throw_false"])
                    monkeys[monkey_to_throw_to]["thrown_items"].append(
                        worry_level)
                monkey["times_inspected"] += 1

    highest_monkeys = [0, 0]
    for monkey in monkeys:

        for i in range(2):
            if monkey["times_inspected"] > highest_monkeys[i]:
                highest_monkeys.insert(i, monkey["times_inspected"])
                highest_monkeys = highest_monkeys[:2]
                break
    return (highest_monkeys[0] * highest_monkeys[1])


print(monkey_bussiness(monkeys()))
print(monkey_bussiness_with_module(monkeys()))
