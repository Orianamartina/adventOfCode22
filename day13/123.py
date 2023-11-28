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


def compare_list_int(a: list, b: int):
    if len(a) == 0:
        return True
    head_a = a.pop(0)
    if type(head_a) is list:
        return compare_list_int(head_a, b)
    return head_a < b


def compare_int_list(a: int, b: list):
    if len(b) == 0:
        return False
    head_b = b.pop(0)
    if type(head_b) is list:
        return compare_int_list(a, head_b)
    return a < head_b


def compare_list(a: list, b: list):
    if len(a) == 0:
        return True

    if len(b) == 0:
        return False

    head_a = a.pop(0)
    head_b = b.pop(0)
    print("comparing: ", head_a, head_b)
    if type(head_a) is list and type(head_b) is list:
        if len(head_a) == 0:
            return True
        return compare_list(head_a, head_b)
    if type(head_a) is list and type(head_b) is int:
        return compare_list(head_a, [head_b])
    if type(head_a) is int and type(head_b) is list:
        return compare_list([head_a], head_b)
    if head_a <= head_b:
        return compare_list(a, b)
    else:

        return head_a < head_b


for i, pair in enumerate(pairs):
    a = pair[0]
    b = pair[1]
    if (compare_list(a, b)):

        right_order_indexes.append(i+1)

print(right_order_indexes)
print(sum(right_order_indexes))
