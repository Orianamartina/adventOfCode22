with open("day12/12input.txt", "r") as file:
    file_contents = file.read()


contents = file_contents.split("\n")
map_height = len(contents)
map_width = len(contents[0])

# global
item_heights = "SabcdefghijklmnopqrstuvwxyzE"


def set_up_graph(contents):

    graph = {}
    counter = 0
    for i in range(map_height):
        for j in range(map_width):
            graph[counter] = []
            if j > 0:
                if item_heights.index(contents[i][j-1]) <= item_heights.index(contents[i][j]) or item_heights.index(contents[i][j-1]) == item_heights.index(contents[i][j])+1:
                    graph[counter].append(counter-1)
            if j < map_width - 1:
                if item_heights.index(contents[i][j+1]) <= item_heights.index(contents[i][j]) or item_heights.index(contents[i][j+1]) == item_heights.index(contents[i][j])+1:
                    graph[counter].append(counter+1)
            if i > 0:
                if item_heights.index(contents[i-1][j]) <= item_heights.index(contents[i][j]) or item_heights.index(contents[i-1][j]) == item_heights.index(contents[i][j])+1:
                    graph[counter].append(counter - map_width)
            if i < map_height - 1:
                if item_heights.index(contents[i+1][j]) <= item_heights.index(contents[i][j]) or item_heights.index(contents[i+1][j]) == item_heights.index(contents[i][j])+1:
                    graph[counter].append(counter + map_width)
            if (i, j) == (20, 0):
                graph[counter].append(counter + 1)
            counter += 1
    return graph


starting_point = 0
ending_point = 0

lowest_coordinates = []


for i in range(map_height):
    for j in range(map_width):
        if contents[i][j] == "a":
            lowest_coordinates.append((i * map_width) + j)
        elif contents[i][j] == "S":
            starting_point = ((i * map_width) + j)
        elif contents[i][j] == "E":
            ending_point = ((i * map_width) + j)

map = set_up_graph(contents)
n = map_height * map_width
g = set_up_graph(contents)


def solve_search(s, e):
    queue = []
    queue.append(s)
    visited = [False for _ in range(n)]
    visited[s] = True
    previous = [None for _ in range(n)]
    while queue:
        node = queue.pop(0)
        neighbors = map[node]
        for next in neighbors:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                previous[next] = node
    return previous


def reconstructPath(s, e, previous):
    path = []
    at = e
    while at is not None:
        path.append(at)
        at = previous[at]
    path = path[::-1]
    if path[0] == s:
        return len(path) - 1
    else:
        return 0


def get_shortest_path(s, e):
    prev = solve_search(s, e)
    return reconstructPath(s, e, prev)


def get_shortest_path_from_any_low_point():
    shortest_path = get_shortest_path(lowest_coordinates[0], ending_point)
    for coordinate in lowest_coordinates:
        current_path = get_shortest_path(coordinate, ending_point)
        if current_path < shortest_path and current_path > 0:
            shortest_path = current_path
    return shortest_path


print(get_shortest_path_from_any_low_point())
print(get_shortest_path(starting_point, ending_point))
