with open("day17/ex.txt", "r") as file:
    file_contents = file.read()


print(file_contents)
"""The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away 
from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one)."""


rocks = [
    ["####"], [".#.", "###", ".#."], ["..#", "..#", "###"], [
        "#", "#", "#", "#"], ["##.", "##."]
]

chamber = {"map":  [["-------"]], "uppermost_rock_line": 0}


def position_rock(rock, chamber, shift):
    position = chamber["uppermost_rock_line"]

    for line in rock:
        chamber["map"][position + 1] = ["." * position]
    print(chamber["map"])


def drop_rocks(chamber):
    rock = rocks[0]

    position_rock(rock, chamber, 3)


drop_rocks(chamber)
