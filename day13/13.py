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


def compare(a, b):

    if type(a) is list and type(b) is list:
        for i in range(len(a)):
            compare([])


print(pairs[0])
right_order_indexes = []

for i, pair in enumerate(pairs):
    print(pair)
    if len(pair[0]) <= len(pair[1]):
        j = 0
        right_order = True
        while j < len(pair[0]):
            if pair[0][j] > pair[1][j]:
                right_order = False
                break
            j += 1

        print(right_order)
