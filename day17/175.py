with open("day17/ex.txt", "r") as file:
    file_contents = file.read()

"""The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away 
from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one)."""
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

# rocks = [
#     ["0011110"], ["0001000", "0011100", "0001000"], ["0011100", "0000100", "0000100",], [
#         "0001000", "0001000", "0001000", "0001000"], ["0011000", "0011000"]
# ]
rocks = [
    [[0, 0, 1, 1, 1, 1, 0]], [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]], [[0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0]], [
        [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]], [[0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0]]
]
# rocks = rocks * 404
# rocks += [[[0, 0, 1, 1, 1, 1, 0]], [[0, 0, 0, 1, 0, 0, 0],
#                                     [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0]],]


class Rock():

    def __init__(self, shape, y):
        self._shape = shape
        self._y = y

    def shift(self, direction):
        new_shape = self._shape
        if direction == "<":
            for i, line in enumerate(self._shape):
                if line[0]:
                    return False
                else:
                    new_shape[i].pop(0)
                    new_shape[i].append(0)
            self._shape = new_shape
        elif direction == ">":
            for i, line in enumerate(self._shape):
                if line[-1]:
                    return False
                else:
                    new_shape[i].pop(-1)
                    new_shape[i].insert(0, 0)
            self._shape = new_shape

    def drop(self, map):
        fits = map.check_if_fits(self)
        while fits:
            previous = self._shape
            self._y -= 1
            self.shift(map.get_next_shift())
            fits = map.check_if_fits(self)
        self._y += 1
        self._shape = previous
        map.settle_rock(self)


class Map():
    def __init__(self):
        self._rows = [["-", "-", "-", "-", "-",
                       "-", "-"], [0, 0, 0, 0, 0, 0, 0]]
        self._width = 7
        self._current_shift = 0
        self._heigth = 1
        self._new_row = [0, 0, 0, 0, 0, 0, 0]
        self._highest_point = 1

    def avalaible_in_row(self, row):
        return self._rows[row]

    def row_is_empty(self, row):
        return len(self._rows[row]) == 0

    def get_next_shift(self):
        self._current_shift += 1
        return file_contents[self._current_shift]

    def check_if_fits(self, rock):
        # y = rock._y
        # x = rock._x
        y = rock._y

        if y >= len(self._rows):
            return True
        for line in rock._shape:
            for i, bit in enumerate(line):
                if (bit and self._rows[y][i]):
                    return False
            y -= 1
        return True

    def settle_rock(self, rock):
        y = rock._y
        for line in rock._shape:
            if y >= len(self._rows):
                self._rows.append(self._new_row)
            self._rows[y] = [a | b for a, b in zip(line, self._rows[y])]
            y += 1
        if y > self._highest_point:
            self._highest_point = y

    def solve(self, rocks):
        total_instances = 2
        counter = 0

        for _ in range(total_instances):
            current_rock = Rock(rocks[counter], self._highest_point + 4)
            current_rock.drop(self)
            counter = (counter + 1) % len(rocks)

        for line in reversed(self._rows):
            print(line)


plane = Map()
plane.solve(rocks)
