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


def compare_list(a, b):
    if type(a) is int and type(b) is int:
            
        if a > b: return -1
        elif a == b: return 0
        else: return 1

    if type(a) is int:
        a = [a] 
    if type(b) is int:
        b = [b]
    shortest_list = min( len(a),len(b))
    for i in range(shortest_list):
        is_ordered = compare_list(a[i], b[i])
        if is_ordered == 0: continue
        else: return is_ordered
    return(compare_list(len(a), len(b)))

for i, pair in enumerate(pairs, start=1):

    if compare_list(*pair) == 1:
        right_order_indexes.append(i)

print(sum(right_order_indexes))
