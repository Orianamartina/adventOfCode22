with open("day15/15input.txt", "r") as file:
    file_contents = file.read()
import re
from time import time
from collections import defaultdict

start = time()

pattern = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)

parsed_input = pattern.findall(file_contents)

coordinates = []
for line in parsed_input:
    x1, y1, x2, y2 = line
    coordinates.append({"sensor": (int(x1), int(y1)),
                       "beacon": (int(x2), int(y2))})


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


pair_distances = []

for pair in coordinates:
    sensor, beacon = pair.values()
    pair_distances.append(manhattan_distance(
        sensor[0], sensor[1], beacon[0], beacon[1]))


def positions_that_dont_contain_beacons_in(row, map):
    empty_coordinates = set()
    used_x = set()
    for i, coordinate in enumerate(map):
        sensor, beacon = coordinate.values()
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon

        beacon_distance = pair_distances[i]

        limit = max(beacon_distance - abs(row - sensor_y), 0)
        if sensor_y == row:
            used_x.add(sensor_x)
        if beacon_y == row:
            used_x.add(beacon_x)
        for i in range(sensor_x - limit, sensor_x + limit + 1):
            if i not in used_x:
                empty_coordinates.add(i)
    return len(empty_coordinates)


# part 2:

map = coordinates


def find_signal(map):
    counter = 1
    several_intersections = []
    for i, coordinate in enumerate(map):
        sensor, beacon = coordinate.values()
        sensor_x, sensor_y = sensor

        print("Analyzing: ", counter, "/", len(pair_distances))
        beacon_distance = pair_distances[i] + 1
        several_intersections.append([])
        generate_points_with_manhattan_distance(
            sensor_x, sensor_y, beacon_distance, several_intersections, i
        )
        counter += 1
    for i, perimeter in enumerate(several_intersections):
        for point in perimeter:
            counter = 0
            for j, coordinate in enumerate(map):
                if j == i:
                    continue
                distance = manhattan_distance(
                    point[0], point[1], coordinate["sensor"][0], coordinate["sensor"][1])
                if distance <= pair_distances[j]:
                    break
                else:
                    counter += 1
            if counter == len(map)-1:
                return point


def generate_points_with_manhattan_distance(
    central_x, central_y, radius, several_intersections, i
):
    limit = 4000000
    for x in range(central_x - radius, central_x + radius + 1):
        if x > 0 and x < limit:
            possible_y_values = radius - abs(x - central_x)
            y1 = central_y + possible_y_values
            y2 = central_y - possible_y_values
            c = []
            if y1 < limit and y1 > 0:
                c.append((x, y1))
            if y2 < limit and y2 > 0:
                c.append((x, y2))
            several_intersections[i] += c


print("15.1", positions_that_dont_contain_beacons_in(
    2000000, coordinates))
print("Part 2:")
part_two = list(find_signal(map))
print("15.2", (part_two[0] * 4000000) + part_two[1])

end = time()

print(end-start)
