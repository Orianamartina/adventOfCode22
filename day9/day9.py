with open("day9/9input.txt", "r") as file:
    file_contents = file.readlines()

from math import sqrt

def instructions():
    instructions = []
    for content in file_contents:
        instructions.append(content.split(" "))
    return instructions

def distance_between_two_points(p1, p2):
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    return sqrt((x1 - x2)**2 + (y1 - y2) **2)

class Coordenate():
    def __init__(self, x, y):
        self._x = x
        self._y = y
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    
class Tail():
    def __init__(self, x, y):
        self._current_position = Coordenate(x, y)
        self._previous_position = Coordenate(x, y)

    def follow(self, head):
        x,y = head.current_position.x, head.current_position.y
        self_x, self_y = self._current_position.x, self._current_position.y, 
        self._previous_position = self._current_position
        distance =distance_between_two_points(head.current_position, self._current_position)
        if distance >= 2 and distance < 3:
            self._current_position = head._previous_position
        elif distance < 2:
            pass
        """elif distance == 2:
            print("holaaa")
            move_x = (self_x - x) 
            move_y = (self_y - y)
            print("move x", move_x)
            print("move_y", move_y)
            if self_x - x == 2:
                self._current_position["x"] -= 1
            elif self_x - x == -2:
                self._current_position["x"] += 1
            if self_y-y == 2:
                self._current_position["y"] -= 1
            elif self_y-y == -2:
                self._current_position["y"] += 1
"""
            

class Head():
    def __init__(self, x,y):
        self._previous_position = Coordenate(x,y)
        self._current_position = Coordenate(x,y)

    @property
    def current_position(self):
        return self._current_position
    
    def move_to(self, direction):
        self._previous_position = self._current_position
        x, y = direction.values()
        self._current_position._x += x 
        self._current_position._y += y


directions = {
    "U": {"x": 0, "y":1},
    "D": {"x": 0, "y":-1},
    "R": {"x": 1, "y":0},
    "L": {"x": -1, "y": 0}
}

def add_visited_coordenates(cooordenate, visited_coordenates):
    for visited_coordenate in visited_coordenates:
        if coordenate.x == visited_coordenate.x and cooordenate.y == visited_coordenate.y:
            break
    if cooordenate not in visited_coordenates:
        visited_coordenates.append(cooordenate)
        print(cooordenate)

def simulate_motions(list_of_motions, head:Head):
    visited_coordenates = []
    for motion in list_of_motions:
        direction, ammount = motion
        for i in range(int(ammount)):
            head.move_to(directions[direction])
            tail.follow(head)
            add_visited_coordenates(tail._current_position,visited_coordenates)

    return len(visited_coordenates)


head = Head(0, 0)
tail = Tail(0, 0)
print(simulate_motions(instructions(), head))

