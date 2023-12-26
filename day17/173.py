with open("day17/ex.txt", "r") as file:
    file_contents = file.read()


print(file_contents)
"""The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away 
from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one)."""


rocks = [
    ["####"], [".#.", "###", ".#."], ["###", "..#", "..#",], [
        "#", "#", "#", "#"], ["##.", "##."]
]

chamber = {"map":  ["#" * 7], "upper": 1}


def get_shift(i):
    if file_contents[i] == ">":
        return 1
    else:
        return -1


def drop_one(rock, x, y, chamber):
    for line in rock:
        if y < len(chamber):
            print("wenas")
            return "#" not in chamber[y][x:x+len(rock)]
    return True


def rest_rock(rock, x, y, chamber):
    for line in rock:
        if y >= len(chamber):
            chamber.append("")
        h1 = chamber[y][:x]
        h2 = line
        h3 = chamber[y][:x+len(line)]
        chamber[y] = h1 + h2 + h3
        y += 1


def drop_rocks(chamber):

    i = 0

    # tick:
    for rock in rocks:
        x = 2
        rock_is_resting = False
        y = chamber["upper"] + 4
        while not rock_is_resting:
            print(i)
            shift = get_shift(i)
            x += shift
            if drop_one(rock, x, y, chamber["map"]):
                print(drop_one(rock, x, y, chamber["map"]))
                y -= 1
                i += 1
            else:
                rest_rock(rock, x, y, chamber["map"])
                if y > chamber["upper"]:
                    chamber["upper"] = y
                rock_is_resting = True


drop_rocks(chamber)

for line in chamber["map"]:
    print(line)
