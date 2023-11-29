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


"""
Packet data consists of lists and integers. 
Each list starts with [, ends with ], 
and contains zero or more comma-separated values 
(either integers or other lists). 
Each packet is always a list and appears on its own line.

"""

right_order_indexes = []


def compare_list(a, b):
    if type(a) is int and type(b) is int:
        return (a > b) - (a < b)
    if type(a) is int and type(b) is list:
        return compare_list([a], b)
    if type(a) is list and type(b) is int:
        return compare_list(a, [b])
    if type(a) is list and type(b) is list:
        for it in map(compare_list, a, b):
            if it:
                return it
            return compare_list(len(a), len(b))


def compare_list(a: list, b: list):
    if len(a) == 0 and len(b) > 0:
        return True

    if len(b) == 0 and len(a) > 0:
        return False

    if len(b) == 0 and len(a) == 0:
        return True
    head_a = a.pop(0)
    head_b = b.pop(0)

    if type(head_a) is list and type(head_b) is list:
        return compare_list(head_a, head_b)
    if type(head_a) is list and type(head_b) is int:
        head_b = [head_b]
        return compare_list(head_a, head_b)
    if type(head_a) is int and type(head_b) is list:
        head_a = [head_a]
        return compare_list(head_a, head_b)
    if head_a == head_b:
        return compare_list(a, b)


for i, pair in enumerate(pairs):
    a = pair[0]
    b = pair[1]
    if compare_list(*pair) == -1:
        right_order_indexes.append(i)

print(right_order_indexes)
print(sum(right_order_indexes))
