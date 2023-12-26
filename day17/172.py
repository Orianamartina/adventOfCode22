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
print(chamber["map"])


def get_shifts(s, e, length):
    shift = 2
    for i in range(s, e):

        if file_contents[i] == ">" and shift + length < 7:
            shift += 1
        else:
            shift -= 1
    return shift


def line_fits(e, s, y):
    for i in range(e, s):
        if i not in chamber["map"][y]:
            return False
    return True


def rock_fits(rock, e, s, y):
    for line in rock:
        if not line_fits(e, s, y):
            return False
        y += 1
    return True


def position_rock(rock, y, x):
    for line in rock:
        print(x, y)
        for i in range(x, x+len(line)):
            while y < len(chamber["map"]):
                chamber["map"].append([0, 1, 2, 3, 4, 5, 6])
            chamber["map"][y].remove(i)
            if y > chamber["upper"]:
                chamber["upper"] = y


def drop_rock():
    current_flow = 0
    for rock in rocks:
        length = len(rock[0])
        highest_point = chamber["upper"]
        print(rock[0])
        i = 4

        x = get_shifts(current_flow, current_flow + i, length)
        previous = x
        fits = rock_fits(rock, x, x+length, highest_point)
        while fits:
            i += 1
            previous = x
            x = get_shifts(current_flow, current_flow + i, length)
            highest_point -= 1
            fits = rock_fits(rock, x, x+length, highest_point)
        position_rock(rock, highest_point + 1, previous)
        print(chamber["map"])


drop_rock()
