import matplotlib.pyplot as plt
import numpy as np
import re
with open("day15/ex.txt", "r") as file:
    file_contents = file.read()

pattern = re.compile(
    r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

matches = pattern.findall(file_contents)

coordinates = []
for match in matches:
    x1, y1, x2, y2 = match
    coordinates.append({"sensor": (x1, y1), "beacon": (x2, y2)})


def scale_coordinates(coordinates, scale_factor):
    return [(x // scale_factor, y // scale_factor) for x, y in coordinates]


def plot_manhattan_circumferences(centers, perimeters, scale_factor=1):
    plt.figure(figsize=(8, 8))

    for center, perimeter_points in zip(centers, perimeters):
        # Scale down the coordinates
        scaled_center = (center[0] // scale_factor, center[1] // scale_factor)
        scaled_perimeter = scale_coordinates(perimeter_points, scale_factor)

        # Plot the Manhattan geometry circumference
        plt.scatter(*zip(*scaled_perimeter),
                    label=f'Perimeter Points ({center[0]}, {center[1]})')
        plt.scatter(*scaled_center, color='red')

    plt.title('Manhattan Geometry Circumferences')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()


def generate_points_with_manhattan_distance(central_x, central_y, radius, points):

    for x in range(central_x - radius, central_x + radius + 1):
        possible_y_values = radius - abs(x - central_x)
        for y in (central_y + possible_y_values, central_y - possible_y_values):
            points[(central_x, central_y)].append((x, y))


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


points = {}
for coordinate in coordinates:
    sensor, beacon = coordinate.values()
    print(sensor, beacon)
    sensor_x, sensor_y = int(sensor[0]), int(sensor[1])
    beacon_x, beacon_y = int(beacon[0]), int(beacon[1])
    points[(sensor_x, sensor_y)] = []
    beacon_distance = manhattan_distance(
        sensor_x, sensor_y, beacon_x, beacon_y) + 1

    generate_points_with_manhattan_distance(
        sensor_x, sensor_y, beacon_distance,  points)


plot_manhattan_circumferences(points.keys(), points.values())

# import numpy as np
# import matplotlib.pyplot as plt


# def get_manhattan_perimeter(center, manhattan_distance):
#     perimeter_points = set()

#     for i in range(-manhattan_distance, manhattan_distance + 1):
#         x = center[0] + i
#         y1 = center[1] + manhattan_distance - abs(i)
#         y2 = center[1] - manhattan_distance + abs(i)

#         perimeter_points.add((x, y1))
#         perimeter_points.add((x, y2))

#     for i in range(-manhattan_distance + 1, manhattan_distance):
#         y = center[1] + i
#         x1 = center[0] + manhattan_distance - abs(i)
#         x2 = center[0] - manhattan_distance + abs(i)

#         perimeter_points.add((x1, y))
#         perimeter_points.add((x2, y))

#     return list(perimeter_points)


# # Example usage
# center_point = (0, 0)
# manhattan_distance = 3

# manhattan_perimeter_points = get_manhattan_perimeter(
#     center_point, manhattan_distance)

# # Plot the Manhattan perimeter points
# plt.figure(figsize=(8, 8))
# plt.scatter(*zip(*manhattan_perimeter_points),
#             label='Manhattan Perimeter Points')
# plt.scatter(*center_point, color='red', label='Center Point')
# plt.title(f'Manhattan Perimeter (Distance={manhattan_distance})')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.grid(True)
# plt.show()
