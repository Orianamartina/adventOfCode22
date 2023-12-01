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
r = []


def compare(a: list, b: list):

    if len(a) == 0:
        return True

    if len(b) == 0:
        return False
    head_a = a.pop(0)
    head_b = b.pop(0)
    if type(head_a) is list and type(head_b) is list:
        return compare(head_a, head_b)
    if type(head_a) is list and type(head_b) is int:
        return compare(head_a, [head_b])
    if type(head_a) is int and type(head_b) is list:
        return compare([head_a], head_b)
    if head_a == head_b:
        return compare(a, b)

    return head_a < head_b


for i, pair in enumerate(pairs, start=1):

    if compare(*pair) == 1:
        r.append(i)
    if i == 84:
        print(pair)
    if i == 102:
        print(pair)

print(r)
print(sum(r))
