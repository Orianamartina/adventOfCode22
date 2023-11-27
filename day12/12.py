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


def get_starting_point():
    for i in range(map_height):
        for j in range(map_width):
            if contents[i][j] == "S":
                return ((i * map_width) + j)


def get_highest_point():
    for i in range(map_height):
        for j in range(map_width):
            if contents[i][j] == "E":
                return ((i * map_width) + j)


starting_point = get_starting_point()
ending_point = get_highest_point()

possible_paths = []

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
        return path
    else:
        return 0


def get_shortest_path():
    prev = solve_search(starting_point, ending_point)
    return reconstructPath(starting_point, ending_point, prev)


print(len(get_shortest_path()))
