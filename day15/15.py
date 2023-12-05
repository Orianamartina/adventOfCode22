with open("day15/15input.txt", "r") as file:
    file_contents = file.read()
import re

import time
start_time = time.time()
pattern = re.compile(
    r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

matches = pattern.findall(file_contents)


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


coordinates = []
for match in matches:
    x1, y1, x2, y2 = match
    coordinates.append({"sensor": (x1, y1), "beacon": (x2, y2)})

min_x = 0
max_x = 0

goal = 2000000

for position in coordinates:
    sensor, beacon = position.values()
    sensor_x = int(sensor[0])
    beacon_x = int(beacon[0])
    max_x = max(max_x, sensor_x, beacon_x)
    min_x = min(min_x, beacon_x, sensor_x)

empty_coordinates = set()


for position in coordinates:
    sensor, beacon = position.values()
    sensor_x, sensor_y = int(sensor[0]), int(sensor[1])
    beacon_x, beacon_y = int(beacon[0]), int(beacon[1])

    distance = manhattan_distance(sensor_x, beacon_x, sensor_y, beacon_y)
    print(sensor, beacon)
    for i in range(min_x, max_x):

        if manhattan_distance(sensor_x, sensor_y, i, goal) <= distance:
            empty_coordinates.add(i)


end_time = time.time()
print("elapsed time", end_time - start_time, "seconds")
print(len(empty_coordinates))
4171158
4476418
