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


"""def compare(a, b):
    if a.isdigit() and b.isdigit():
        return a <= b
    if a.startswith("[") and b.startswith("["):
        return a[1] < b[1]
    else:
        return ("Weno no")


for i, pair in enumerate(contents):
    packets = pair.split("\n")

    packet_one = packets[0].split(",")
    packet_two = packets[1].split(",")
    # if len(packet_one) > len(packet_two):
    #     continue
    # else:
    print(packet_one)
    print(packet_two)
    c = 0
    stack = 0
    print(compare(packet_one[c], packet_two[c]))"""

right_order_indexes = []


def compare_if_is_right_order(a, b):
    print("comparing", a, b)
    if type(a) is int and type(b) is int:
        print("int")
        print(a, b)
        return a <= b
    if type(a) is list and type(b) is list:
        print("list")
        if len(a) == 0:
            return True
        if len(b) == 0:
            return False
        if len(b) < len(a):
            return False
        else:
            for i, item in enumerate(a):
                compare_if_is_right_order(item, b[i])

    else:
        print("eee")
        if type(a) is not list:
            a = [a]
        if type(b) is not list:
            b = [b]
        return compare_if_is_right_order(a, b)


for i, pair in enumerate(pairs):
    a = pair[0]
    b = pair[1]

    c = 0
    if len(a) == 0:
        right_order_indexes.append(i+1)
        continue
    order = True

    while c < len(a):
        if c == len(b):
            break

        elif not compare_if_is_right_order(a[c], b[c]):

            order = False
        c += 1
    if order:
        right_order_indexes.append(i+1)


print(right_order_indexes)
