with open("day9/9input.txt", "r") as file:
    file_contents = file.readlines()

from math import sqrt

class Knot:
    def __init__(self, x, y):
        self._current_position = [x, y]

    @property
    def current_position(self):
        return self._current_position

    def move_to(self, direction):
        self._current_position[0] += ((direction == "R") - (direction == "L"))
        self._current_position[1] += ((direction == "U") - (direction == "D"))

    def follow(self, head):
        head_x, head_y = head._current_position
        x, y = self._current_position
        _x = abs(head_x - x)
        _y = abs(head_y - y)
        if _x > 1 or _y > 1:
           
            self._current_position[0]+= (head_x > x) - (head_x < x)
            self._current_position[1]+= (head_y > y) - (head_y < y) 

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


def move(knot, direction):

    knot[0] += ((direction == "R") - (direction == "L"))
    knot[1] += ((direction == "U") - (direction == "D"))
    return knot

def follow(head, knot):

    head_x, head_y = head
    x, y = knot
    _x = abs(head_x - x)
    _y = abs(head_y - y)
    if _x > 1 or _y > 1:
        
        knot[0] += (head_x > x) - (head_x < x)
        knot[1] += (head_y > y) - (head_y < y)
    return knot

def simulate_motions_2(tails):
    visited_coordinates = []
    for motion in file_contents:
        direction, ammount = motion.split()
        for i in range(int(ammount)):
            move(tails[0], direction)
            for j in range(len(tails) - 1):
                tail = tails[j+1]
                head = tails[j]
                tails[j+1] = follow(head, tail)
                    
            coordinate = tails[-1]
            visited_coordinates.append(tuple(coordinate))
    print(visited_coordinates)
    return len(set(visited_coordinates))

ex =[
    ["R", "4"], ["U", "4"], ["L", "3"], ["D", "1"],["R", "4"],["D", "1"], ["L", "5"], ["R", "2"]
]
ex2=[
    ["R", "5"], ["U", "8"], ["L", "8"], ["D", "3"], ["R", "17"], ["D", "10"], ["L", "25"], ["U", "20"]
]


tails = [[0, 0] for _ in range(10)]

#print(simulate_motions(instructions(), head, tail))

print(simulate_motions_2(tails))