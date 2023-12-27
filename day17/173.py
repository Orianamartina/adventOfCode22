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
rocks = [
    ([0b0011110], 0),
    ([0b0001000, 0b0011100, 0b0001000], 1),
    ([0b0011100, 0b0000100, 0b0000100], 0),
    ([0b0010000, 0b0010000, 0b0010000], 0),
    ([0b0011000, 0b0011000], 0),
]
rocks = [
    ["1111"], ["010", "111", "010"], ["111", "001", "001",], [
        "1", "1", "1", "1"], ["11", "11"]
]
rocks = rocks * 404
rocks += ["1111"], ["010", "111", "010"]
chamber = {"map":  [[], [0, 1, 2, 3, 4, 5, 6]], "upper": 0}


class Rock():

    def __init__(self, shape, y):
        self._shape = shape[0]
        self._max_width = shape[0][shape[1]]
        self._x = 2
        self._y = y

    def shift(self, direction):
        if direction == ">" and self._max_width[0]:
            pass

    def drop(self, map):
        if map.check_if_fits(self):
            self._y -= 1


class Map():
    def __init__(self):
        self._rows = [["-", "-", "-", "-", "-",
                       "-", "-"], [1, 1, 1, 1, 1, 1, 1]]
        self._width = 7
        self._current_shift = 0
        self._heigth = 1
        self._new_row = [1, 1, 1, 1, 1, 1, 1]

    def avalaible_in_row(self, row):
        return self._rows[row]

    def row_is_empty(self, row):
        return len(row) == 0

    def get_next_shift(self):
        self._current_shift += 1
        return file_contents[self._current_shift]

    def line_fits(self, x, y, line):

        for i in line:
            if not self.avalaible_in_row(y)[x+i]:
                return False
            if y > self._heigth:
                self._rows.append(self._new_row)
                return True
        return True

    def check_if_fits(self, rock):
        # y = rock._y
        # x = rock._x
        for line in rock._shape:
            if not self._line_fits(rock._x, rock._y, line):
                return False
        return True

    def tick(self, rock: Rock):
        rock.shift(self.get_next_shift())
        rock.drop()
