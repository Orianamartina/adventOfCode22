with open("day9/9input.txt", "r") as file:
    file_contents = file.readlines()

from math import sqrt


class Coordinate:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Coordenada {self.x, self.y}"

class Knot:
    def __init__(self, x, y):
        self._previous_position = Coordinate(x, y)
        self._current_position = Coordinate(x, y)

    @property
    def current_position(self):
        return self._current_position

    def move_to(self, direction):
        self._previous_position = Coordinate(
            self._current_position.x, self._current_position.y
        )

        self._current_position._x += (direction == "R") - (direction == "L")
        self._current_position._y += (direction == "U") - (direction == "D")

    def follow(self, head):
        distance = distance_between_two_points(
            head.current_position, self._current_position
        )
        self._previous_position = Coordinate(self._current_position.x, self._current_position.y)
        head_x, head_y = head._current_position.x, head._current_position.y
        x, y = self._current_position.x, self._current_position.y
        if abs(head_x - y) or abs(head_y - y) > 1:
           
            new__x = self._current_position._x +  (head_x > x) - (head_x < x)
            new_y = self._current_position._y + (head_y > y) - (head_y < y) 
            self._current_position = Coordinate(new__x, new_y)
            print(self._current_position)



def instructions():
    instructions = []
    for content in file_contents:
        instructions.append(content.split(" "))
    return instructions


def distance_between_two_points(p1, p2):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def add_visited_coordinates(coordinate, visited_coordinates):
    if coordinate not in visited_coordinates:
        visited_coordinates.append(coordinate)


def simulate_motions(list_of_motions, head, tail):
    visited_coordinates = []
    for motion in list_of_motions:
        direction, ammount = motion
        for _ in range(int(ammount)):
            head.move_to(direction)
            tail.follow(head)
            coordinate = tail.current_position
            if coordinate not in visited_coordinates:
                visited_coordinates.append(coordinate)
                

    return len(visited_coordinates)

def simulate_motions_2(list_of_motions, tails):
    visited_coordinates = []
    for motion in list_of_motions:
        
        direction, ammount = motion
        for i in range(int(ammount)):
            print("-------------")
            for j, tail in enumerate(tails):
                if j == 0:
                    tails[0].move_to(direction)
                if j < len(tails) - 1:
                    head = tails[j]
                    tail = tails[j+1]
                    tail.follow(head)
                    print(f'Head:  {j}, {head._current_position} Tail: {j+1}  {tail._current_position}')
                else:
                    coordinate = tails[j].current_position
                    if coordinate not in visited_coordinates:
                        visited_coordinates.append(coordinate)
                
    return len(visited_coordinates)

ex =[
    ["R", "4"], ["U", "4"], ["L", "3"], ["D", "1"],["R", "4"],["D", "1"], ["L", "5"], ["R", "2"]
]
ex2=[
    ["R", "5"], ["U", "8"], ["L", "8"], ["D", "3"], ["R", "17"], ["D", "10"], ["L", "25"], ["U", "20"]
]

head = Knot(0, 0)
tail = Knot(0, 0)
tails = [Knot(0,0) for _ in range(9)]

print(simulate_motions(instructions(), head, tail))

#print(simulate_motions_2(ex1, tails))