with open("day17/ex.txt", "r") as file:
    file_contents = file.read()


print(file_contents)
"""The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away 
from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one)."""


rocks = [
    ["####"], [".#.", "###", ".#."], ["###", "..#", "..#",], [
        "#", "#", "#", "#"], ["##.", "##."]
]

chamber = {"map":  [["-" * 7]], "uppermost_rock_line": 1}


def position_rock(rock, chamber, shift):

    for line in rock:
        print(line, shift)
        line_length = shift + len(max(rock))
        rest = 7 - line_length
        chamber["map"].insert(0, [])
        chamber["map"][0] = ["." * shift + line + "." * rest]
        chamber["uppermost_rock_line"] += 1


def get_shift(max_line, ls):
    shift = 2
    print(max_line)
    for i in range(ls, ls+4):
        print(file_contents[i])
        if file_contents[i] == ">" and shift + 1 + max_line <= 7:
            shift += 1
        else:
            shift -= 1
    return shift


def drop_rocks(chamber):
    last_shift_index = 0
    for rock in rocks:
        max_line = len(max(rock))
        shift = get_shift(max_line, last_shift_index)
        position_rock(rock, chamber, shift)
        last_shift_index += 4


drop_rocks(chamber)

for line in chamber["map"]:
    print(line)
