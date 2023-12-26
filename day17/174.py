with open("day17/ex.txt", "r") as file:
    file_contents = file.read()


print(file_contents)
"""The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away 
from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one)."""


rocks = [
    ["####"], [".#.", "###", ".#."], ["###", "..#", "..#",], [
        "#", "#", "#", "#"], ["##.", "##."]
]
empty_line = ['-', '-', '-', '-', '-', '-', '-']
chamber = {"map":  [empty_line, empty_line,
                    empty_line, empty_line, empty_line, empty_line], "upper": 1}

print(chamber["map"])


def get_shifts(s, e, length):
    shift = 0
    for i in range(s, e):
        if file_contents[i] == ">" and shift + length < 7:
            shift += 1
        else:
            shift -= 1
    return shift


def drop_one(rock, x, y, chamber):
    for line in rock:
        if y < len(chamber):
            if "#" in chamber[y][x:x+len(line)]:
                return False
            y += 1
    return True


def rest_rock(rock, x, y, chamber):
    for line in rock:
        if y < len(chamber):
            chamber.append(empty_line)
        for i in range(x, x+len(rock[0])):
            chamber[y][i] = line[i-x]


def drop_rocks(chamber):
    i = 0
    rock = rocks[0]
    length = len(rock[0])
    x = 2 + get_shifts(i, i+4, length)
    y = chamber["upper"]

    while "#" not in chamber["map"][y][x]:
        print("ee")
        y -= 1
        x += get_shifts(i, i, length)
        print(x)
    rest_rock(rock, x, y, chamber["map"])


drop_rocks(chamber)

for line in chamber["map"]:
    print(line)
