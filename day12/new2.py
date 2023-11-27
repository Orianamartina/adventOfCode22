import collections

with open("day12/12input.txt", "r") as file:
    file_contents = file.read()

file_contents = file_contents.split("\n")

contents = []
for i in range(len(file_contents)):
    contents.append(list(file_contents[i]))

map_height = len(contents)
map_width = len(contents[0])

starting_point = 0
ending_point = 0

for i in range(map_height):
    for j in range(map_width):
        if contents[i][j] == "S":
            contents[i][j] = "a"
            starting_point = (i, j)

        if contents[i][j] == "E":
            contents[i][j] = "z"
            ending_point = (i, j)


def get_neighbors(node):
    y, x = node
    neighbors = []
    current = ord(contents[y][x])
    if y < map_height - 1 and (ord(contents[y+1][x]) <= current or ord(contents[y+1][x]) == current + 1):
        neighbors.append((y+1, x))
    if y > 0 and (ord(contents[y-1][x]) <= current or ord(contents[y-1][x]) == current + 1):
        neighbors.append((y-1, x))
    if x < map_width - 1 and (ord(contents[y][x+1]) <= current or ord(contents[y][x+1]) == current + 1):
        neighbors.append((y, x+1))
    if x > 0 and (ord(contents[y][x-1]) <= current or ord(contents[y][x-1]) == current + 1):
        neighbors.append((y, x-1))

    return neighbors


def get_shortest_path():
    n = map_height * map_width

    queue = []
    queue.append(starting_point)
    visited = []
    visited.append(starting_point)
    previous = {}
    while queue:
        node = queue.pop(0)
        neighbors = get_neighbors(node)
        for next in neighbors:
            if next not in visited:
                queue.append(next)
                visited.append(next)
                previous[next] = node

    path = []
    at = ending_point

    while at is not starting_point:
        path.append(at)
        at = previous[at]

    return len(path)


print(get_shortest_path())
