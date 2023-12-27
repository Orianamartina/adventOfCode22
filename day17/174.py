with open("day17/ex.txt", "r") as file:
    file_contents = file.read()

"""The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away 
from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one)."""


rocks = [
    ["1111"], ["010", "111", "010"], ["111", "001", "001",], [
        "1", "1", "1", "1"], ["11", "11"]
]
rocks = rocks * 404
rocks += ["1111"], ["010", "111", "010"]
chamber = {"map":  [[], [0, 1, 2, 3, 4, 5, 6]], "upper": 0}
"""
['..##...']
['..##...']
['....#..']
['....#..']
['....#..']
['....#..']
['..#....']
['..#....']
['###....']
['...#...']
['..###..']
['...#...']
['..####.']
['-------']
"""
"""
['.......']
['.......']
['.......']
['.......']
['....##.']
['....##.']
['....#..']
['..#.#..']
['..#.#..']
['#####..']
['..###..']
['...#...']
['..####.']
['-------']
"""
"""
['.......']
['.......']
['.......']
['.......']
['##.....']
['##.....']
['..#...#']
['..#...#']
['..#.###']
['..##...']
['..###..']
['...#...']
['..####.']
['-------']
"""


def get_shifts(s, e, length):
    shift = 2
    for i in range(s, e):
        if file_contents[i] == ">" and shift + length < 7:
            shift += 1
        else:
            shift -= 1
    return shift


def line_fits(line, s, y):
    # s es el valor de x donde empieza la seccion que queremos mirar
    # line = 001
    if y >= len(chamber["map"]):
        return True
    for i, dot in enumerate(line):
        if dot and s+i not in chamber["map"][y]:
            return False
    return True


def rock_fits(rock, s, y):
    for line in rock:
        if not line_fits(line, s, y):
            return False
        y += 1
    return True


def position_rock(rock, y, x):
    for line in rock:
        for i, char in enumerate(line):
            if y >= len(chamber["map"]):
                chamber["map"].append([0, 1, 2, 3, 4, 5, 6])
            if int(char):
                chamber["map"][y].remove(x+i)
        y += 1

    if y > chamber["upper"]:
        chamber["upper"] = y


def drop_rock():
    current_flow = 0
    for rock in rocks:
        length = len(rock[0])
        current_point = chamber["upper"]
        i = 4
        x = get_shifts(current_flow, current_flow + i, length)
        previous = x
        fits = rock_fits(rock, x, current_point)

        while fits:
            i += 1
            current_flow = i
            previous = x
            current_point -= 1
            x = get_shifts(current_flow, current_flow + i, length)

            fits = rock_fits(rock, x, current_point)
        position_rock(rock, current_point + 1, previous)


drop_rock()
print(len(chamber["map"]))
# print(chamber["map"].reverse())
# for line in chamber["map"]:
#     print(line)


# 3237 too low
