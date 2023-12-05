with open("day15/15input.txt", "r") as file:
    file_contents = file.read()
import re


pattern = re.compile(
    r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

matches = pattern.findall(file_contents)

coordinates = []
for match in matches:
    x1, y1, x2, y2 = match
    coordinates.append({"sensor": (x1, y1), "beacon": (x2, y2)})

empty_coordinates = set()

goal = 2000000
# goal = 10


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


used_x = []

for coordinate in coordinates:
    sensor, beacon = coordinate.values()
    sensor_x, sensor_y = int(sensor[0]), int(sensor[1])
    beacon_x, beacon_y = int(beacon[0]), int(beacon[1])

    beacon_distance = manhattan_distance(
        sensor_x, sensor_y, beacon_x, beacon_y)
    y_distance = goal - beacon_y

    limit = max(beacon_distance - abs(goal - sensor_y), 0)
    if sensor_y == goal:
        used_x.append(sensor_x)
    if beacon_y == goal:
        used_x.append(beacon_x)
    for i in range(sensor_x - limit, sensor_x + limit + 1):
        if i not in used_x:
            empty_coordinates.add(i)


print(len(empty_coordinates))
