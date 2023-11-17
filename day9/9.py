with open("day9/9input.txt", "r") as file:
    file_contents = file.readlines()


def move(knot, direction):
    knot[0] += (direction == "R") - (direction == "L")
    knot[1] += (direction == "U") - (direction == "D")
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


def simulate_motions(rope_length):
    tails = [[0, 0] for _ in range(rope_length)]
    visited_coordinates = []
    for motion in file_contents:
        direction, ammount = motion.split()
        for i in range(int(ammount)):
            move(tails[0], direction)
            for j in range(len(tails) - 1):
                tail = tails[j + 1]
                head = tails[j]
                tails[j + 1] = follow(head, tail)

            coordinate = tails[-1]
            visited_coordinates.append(tuple(coordinate))
    return len(set(visited_coordinates))


print(simulate_motions(2))

print(simulate_motions(10))
