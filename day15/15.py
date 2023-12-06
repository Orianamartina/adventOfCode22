with open("day15/ex.txt", "r") as file:
    file_contents = file.read()
import re
from collections import defaultdict


pattern = re.compile(
    r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

matches = pattern.findall(file_contents)

coordinates = []
for match in matches:
    x1, y1, x2, y2 = match
    coordinates.append({"sensor": (x1, y1), "beacon": (x2, y2)})


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def positions_that_dont_contain_beacons_in(row, map):
    empty_coordinates = set()
    used_x = []

    for coordinate in map:
        sensor, beacon = coordinate.values()
        sensor_x, sensor_y = int(sensor[0]), int(sensor[1])
        beacon_x, beacon_y = int(beacon[0]), int(beacon[1])

        beacon_distance = manhattan_distance(
            sensor_x, sensor_y, beacon_x, beacon_y)

        limit = max(beacon_distance - abs(row - sensor_y), 0)
        if sensor_y == row:
            used_x.append(sensor_x)
        if beacon_y == row:
            used_x.append(beacon_x)
        for i in range(sensor_x - limit, sensor_x + limit + 1):
            if i not in used_x:
                empty_coordinates.add(i)

    return (len(empty_coordinates))


# print(positions_that_dont_contain_beacons_in(2000000, coordinates))

# part 2:

map = coordinates
# map = [{"sensor": (0, 0), "beacon": (0, 3)}, {
#     "sensor": (4, 0), "beacon": (6, 0)}]


def find_signal(map):
    fours = []

    available = defaultdict(lambda: 0)
    for coordinate in map:

        sensor, beacon = coordinate.values()
        print(sensor)
        sensor_x, sensor_y = int(sensor[0]), int(sensor[1])
        beacon_x, beacon_y = int(beacon[0]), int(beacon[1])
        beacon_distance = manhattan_distance(
            sensor_x, sensor_y, beacon_x, beacon_y) + 1

        x = beacon_distance * -1
        y = 0

        while x != 0:
            c = (sensor_x + x, sensor_y + y)
            available[c] += 1
            y += 1
            x += 1
            print(available[c])
            if available[c] == 4:
                return c

        x = 0
        y = beacon_distance
        while x != beacon_distance:
            c = (sensor_x + x, sensor_y + y)
            available[c] += 1
            y -= 1
            x += 1
            if available[c] == 4:
                return c

        x = beacon_distance
        y = 0
        while x != 0:
            c = (sensor_x + x, sensor_y + y)
            available[c] += 1
            y += 1
            x -= 1
            if available[c] == 4:
                return c

        x = 0
        y = beacon_distance * -1
        while x != beacon_distance * -1:
            c = (sensor_x + x, sensor_y + y)
            available[c] += 1
            y += 1
            x -= 1
            if available[c] == 4:
                return c


# print(find_signal(map))

# print((3271544 * 4000000) + 3688993) ño :c
