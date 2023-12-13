with open("day15/15input.txt", "r") as file:
    file_contents = file.read()
import re
from time import time

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


def find_intersection_points(perimeter1, perimeter2):
    intersection_points = []
    for point1 in perimeter1:
        for point2 in perimeter2:
            if point1 == point2:
                intersection_points.append(point1)
            if len(intersection_points) == 2:
                return intersection_points
    if len(intersection_points) > 0:
        return intersection_points


def generate_points_with_manhattan_distance(
    central_x, central_y, radius, several_intersections, i
):
    print(central_x, central_y)
    for x in range(central_x - radius, central_x + radius + 1):
        if x > 0 and x < 4000000:

            possible_y_values = radius - abs(x - central_x)
            y1 = central_y + possible_y_values
            y2 = central_y - possible_y_values

            several_intersections[i] += [(x, y1), (x, y2)]


pair_distances = []

for pair in coordinates:
    sensor, beacon = pair.values()
    pair_distances.append(manhattan_distance(
        sensor[0], sensor[1], beacon[0], beacon[1]))


perimeters = []

for i, pair in enumerate(coordinates):
    sensor, beacon = pair.values()
    perimeters.append([])
    generate_points_with_manhattan_distance(
        sensor[0], sensor[1],  pair_distances[i], perimeters, i)

for i in perimeters:
    print(perimeters)

# intersections = set()
# for i, c_1 in enumerate(perimeters):
#     print(c_1)
#     for j, c_2 in enumerate(perimeters):
#         if i == j:
#             continue
#         found_intersections = find_intersection_points(c_1, c_2)
#         if found_intersections:
#             intersections.update(found_intersections)


# short_intersections = []

# for i, i_1 in enumerate(intersections):
#     two_unit_distanced_intersections = set()
#     for j, i_2 in enumerate(intersections):
#         if manhattan_distance(i_1[0], i_1[1], i_2[0], i_2[1]) == 2:
#             two_unit_distanced_intersections.add(i_1)
#             two_unit_distanced_intersections.add(i_2)
#     short_intersections.append(two_unit_distanced_intersections)


# for i in short_intersections:
#     if len(i) >= 4:
#         print(i)
