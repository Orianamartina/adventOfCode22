with open("day13/13input.txt", "r") as file:
    file_contents = file.read()

import ast

contents = file_contents.split('\n\n')

pairs = []
for pair in contents:
    a = []
    for division in pair.split('\n'):
        a.append(ast.literal_eval(division))
    pairs.append(a)


right_order_indexes = []


def compare(a, b):
    match a, b:
        case int(), int():
            print("cche", a, b)
            is_smaller = b >= a
            print("issmaller", is_smaller)
            return is_smaller
        case list(), int():
            if len(a) >= 1:
                return compare(a[0], b)
        case int(), list():
            return compare([a], b)
        case list(), list():
            if len(a) == 0:
                return True
            if len(b) == 0:
                return False
            else:
                for i, item in enumerate(a):
                    print("aaa")
                    if i == len(b) and len(a) > len(b):
                        return False
                    print("wewewe", item, b[i])
                    if i == len(a) - 1:
                        return compare(item, b[i])
                    else:
                        if not (compare(item, b[i])):
                            return False


for j, pair in enumerate(pairs):
    a = pair[0]
    b = pair[1]

    order = True

    if not compare(a, b):
        print(compare(a, b))
        print("chehceche")
        order = False

    print(order)
    if order:
        right_order_indexes.append(j+1)


print(right_order_indexes)
