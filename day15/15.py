with open("day15/ex.txt", "r") as file:
    file_contents = file.read()
import re


pattern = re.compile(
    r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

matches = pattern.findall(file_contents)

coordinates = []
for match in matches:
    x1, y1, x2, y2 = match
    coordinates.append({"sensor": (x1, y1), "beacon": (x2, y2)})


for position in coordinates:
    sensor, beacon = position.values()
