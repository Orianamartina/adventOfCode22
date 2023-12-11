with open("day15/15input.txt", "r") as file:
    file_contents = file.read()
import re
import time
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


start_time = time.time()
print("part 1", positions_that_dont_contain_beacons_in(2000000, coordinates))

# part 2:

map = coordinates


def find_signal(map):
    coordinates = defaultdict(lambda: 0)
    several_intersections = []
    for coordinate in map:
        sensor, beacon = coordinate.values()
        print(sensor, beacon)
        sensor_x, sensor_y = int(sensor[0]), int(sensor[1])
        beacon_x, beacon_y = int(beacon[0]), int(beacon[1])
        beacon_distance = manhattan_distance(
            sensor_x, sensor_y, beacon_x, beacon_y) + 1

        generate_points_with_manhattan_distance(
            sensor_x, sensor_y, beacon_distance, coordinates, several_intersections)

    possible_beacon_position = set(several_intersections)
    for coordinate in several_intersections:
        for device_pair in map:
            sensor, beacon = device_pair.values()
            sensor_x, sensor_y = int(sensor[0]), int(sensor[1])
            beacon_x, beacon_y = int(beacon[0]), int(beacon[1])

            intersection_distance = manhattan_distance(
                sensor_x, sensor_y, coordinate[0], coordinate[1])
            sensor_beacon_distance = manhattan_distance(
                sensor_x, sensor_y, beacon_x, beacon_y)

            if intersection_distance <= sensor_beacon_distance and coordinate in possible_beacon_position:
                possible_beacon_position.remove(coordinate)
    return possible_beacon_position


def generate_points_with_manhattan_distance(central_x, central_y, radius, coordinates, several_intersections):
    for x in range(central_x - radius, central_x + radius + 1):
        possible_y_values = radius - abs(x - central_x)
        for y in (central_y + possible_y_values, central_y - possible_y_values):
            coordinates[(x, y)] += 1
            if coordinates[(x, y)] >= 4:
                several_intersections.append((x, y))


part_two = list(find_signal(map))
print((part_two[0][0] * 4000000) + part_two[0][1])
end_time = time.time()
print(end_time - start_time)
