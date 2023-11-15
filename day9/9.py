with open("day9/9input.txt", "r") as file:
    file_contents = file.readlines()

instructions = []

for line in file_contents:
    instructions.append(line.split())

def move(direction, coordinates):
    x, y = coordinates
    x = (direction == "R") - (direction == "L")
    y = (direction == "U") - (direction == "D")
    
    return x, y

def follow(knot, head):
    x, y = knot
    hx, hy = head
    if abs(hx - x) > 1 or abs(hy - y) > 1:
        y += (hy > y) - (hy < y)
        x += (hx > x) - (hx < x)
    return x, y


def move(instructions, rope):
    visited_coordenates = []
    
    for line in instructions:
        direction, ammount = line
        for _ in range(int(ammount)):
            for i in range(len(rope)):
                if i == 0:
                    x,y = rope[0]
                    x += (direction == "R") - (direction == "L")
                    y += (direction == "U") - (direction == "D")
                    rope[0] = (x,y)
                    rope[i+1] = follow(rope[i+1], (x,y))
                    print(rope)
                if i == len(rope) -1:
                    visited_coordenates.append(rope[i])
                if i > 0 and i < len(rope) - 1:
                    rope[i+1] = follow(rope[i+1], rope[i])
    return(len(set(visited_coordenates)))

ex =[
    ["R", "4"], ["U", "4"], ["L", "3"], ["D", "1"],["R", "4"],["D", "1"], ["L", "5"], ["R", "2"]
]
rope = [(0, 0) for _ in range(9)]
print(move(instructions[:40], rope))
#move(instructions, rope)