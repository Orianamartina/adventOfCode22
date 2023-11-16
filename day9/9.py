
rope1 = [[0, 0] for _ in range(2)]
rope2 = [[0, 0] for _ in range(10)]

with open("day9/9input.txt", "r") as file:
    file_contents = file.readlines()

def get_tail_coordinate_history(rope):
    visited_coordinates = set([(0, 0)])
    for line in file_contents:
        direction, ammount = line.split()
        ammount = int(ammount)

        for _ in range(ammount):
            dx = (direction == "R") - (direction == "L")
            dy = (direction == "U") - (direction == "D")

            rope[0][0] += dx
            rope[0][1] += dy

            for i in range(len(rope) -1):
                head = rope[i]
                tail = rope[i + 1]

                _x = head[0] - tail[0]
                _y = head[1] - tail[1]

                if abs(_x) > 1 or abs(_y) > 1:
                    if _x == 0:
                        tail[1] += _y // 2
                    elif _y == 0:
                        tail[0] += _x // 2
                    else:
                        tail[0] += 1 if _x > 0 else -1
                        tail[1] += 1 if _y > 0 else -1

            visited_coordinates.add(tuple(rope[-1]))

    print(len(visited_coordinates))


get_tail_coordinate_history(rope1)
get_tail_coordinate_history(rope2)