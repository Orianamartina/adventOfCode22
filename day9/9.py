with open("day9/9input.txt", "r") as file:
    file_contents = file.readlines()

class Knot:
    def __init__(self, x, y):
        self._position = (x,y)

    @property
    def current_position(self):
        return self._current_position

    def move_to(self, direction):
        x, y = direction.values()
        self._current_position._x += x
        self._current_position._y += y

        """    for hx, hy in head:
        if abs(hx - x) > 1 or abs(hy - y) > 1:
            y += (hy > y) - (hy < y)
            x += (hx > x) - (hx < x)
        yield x, y"""

    def follow(self, head):

        head_x, head_y = head._position
        x, y = self._position
        if abs(head_x - y) or abs(head_y - y) > 1:
            self._position._x +=  (head_x > x) - (head_x < x)
            self._position._y += (head_y > y) - (head_y < y)
            print(self._position)

directions = {
    "U": {"x": 0, "y": 1},
    "D": {"x": 0, "y": -1},
    "R": {"x": 1, "y": 0},
    "L": {"x": -1, "y": 0},
}
def instructions():
    instructions = []
    for content in file_contents:
        instructions.append(content.split(" "))
    return instructions

def add_visited_coordinates(coordinate, visited_coordinates):
    if coordinate not in visited_coordinates:
        visited_coordinates.append(coordinate)


def simulate_motions_2(list_of_motions, tails):
    visited_coordinates = []
    for motion in list_of_motions:
        
        direction, ammount = motion
        for i in range(int(ammount)):
            #print("-------------")
            for j, tail in enumerate(tails):
                if j == 0:
                    tails[0].move_to(directions[direction])
                if j < len(tails) - 1:
                    head = tails[j]
                    tail = tails[j+1]
                    tail.follow(head) 
                    #print(f'Head:  {j}, {head._current_position} Tail: {j+1}  {tail._current_position}')
                else:

                    add_visited_coordinates(tails[j].current_position, visited_coordinates)
                


head = Knot(0, 0)
tail = Knot(0, 0)
tails = [Knot(0,0) for _ in range(9)]