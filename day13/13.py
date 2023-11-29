with open("day13/13input.txt", "r") as file:
    file_contents = file.read()

from itertools import zip_longest

import ast

contents = file_contents.split('\n\n')

pairs = []
for pair in contents:
    a = []
    for division in pair.split('\n'):
        a.append(ast.literal_eval(division))
    pairs.append(a)

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
    print("comparing: a", a, "b: ", b)
    if len(a) == 0:
        return True

    if len(b) == 0:
        return False
    head_a = a.pop(0)
    head_b = b.pop(0)
    print("comparing: a", head_a, "b: ", head_b)
    if type(head_a) is list and type(head_b) is list:
        return compare_list(head_a, head_b)
    if type(head_a) is list and type(head_b) is int:
        return compare_list(head_a, [head_b])
    if type(head_a) is int and type(head_b) is list:
        return compare_list([head_a], head_b)
    if head_a == head_b:
        return compare_list(a, b)

    return head_a < head_b


def compare(a, b):
    paired_items = zip_longest(a, b, fillvalue=None)

    answer = None

    for pair in paired_items:
        a, b = pair

    if type(a) is int and type(b) is int:
        return a < b
    if type(a) is list and type(b) is int:
        answer = compare(a, b)
    if type(a) is int and type(b) is list:
        answer = compare([a], b)
    if type(b) is int and type(a) is list:
        answer = compare(a, [b])

    if a == None:
        return True
    if b == None:
        return False

    if answer != None:
        return answer


for i, pair in enumerate(pairs, start=1):

    if compare_list(*pair):
        right_order_indexes.append(i)

    if i == 84:
        print(i)
print(right_order_indexes)
