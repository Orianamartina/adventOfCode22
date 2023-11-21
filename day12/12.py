with open("day12/12input.txt", "r") as file:
    file_contents = file.read()


"""
there could be various path alternatives to follow
we need the shortest one 
"""

contents = file_contents.split("\n")
map_heigth = len(contents)
map_width = len(contents[0])

# global
item_heigths = "SabcdefghijklmnopqrstuvwxyzE"


def set_up_graph(contents):

    graph = []
    counter = 0
    for i in range(map_heigth):
        for j in range(map_width):
            graph.append([])
            if j > 0:
                if item_heigths.index(contents[i][j-1]) == item_heigths.index(contents[i][j]) or item_heigths.index(contents[i][j-1]) == item_heigths.index(contents[i][j])+1:
                    graph[counter].append(counter-1)
            if j < map_width - 1:
                if item_heigths.index(contents[i][j+1]) == item_heigths.index(contents[i][j]) or item_heigths.index(contents[i][j+1]) == item_heigths.index(contents[i][j])+1:
                    graph[counter].append(counter+1)
            if i > 0:
                if item_heigths.index(contents[i-1][j]) == item_heigths.index(contents[i][j]) or item_heigths.index(contents[i-1][j]) == item_heigths.index(contents[i][j])+1:
                    graph[counter].append(counter - map_width)
            if i < map_heigth - 1:
                if item_heigths.index(contents[i+1][j]) == item_heigths.index(contents[i][j]) or item_heigths.index(contents[i+1][j]) == item_heigths.index(contents[i][j])+1:
                    graph[counter].append(counter + map_width)
            counter += 1
    return graph


def get_starting_point():
    for i in range(map_heigth):
        for j in range(map_width):
            if contents[i][j] == "S":
                return ((i * map_width) + j)


def get_highest_point():
    for i in range(map_heigth):
        for j in range(map_width):
            if contents[i][j] == "E":
                return ((i * map_width) + j)


possible_paths = []

map = set_up_graph(contents)

n = map_heigth * map_width
g = set_up_graph(contents)


def solve_search(s):
    queue = []
    queue.append(s)

    visited = [False for _ in range(n)]
    visited[s] = True

    previous = [None for _ in range(n)]
    while not len(queue) == 0:
        node = queue.pop(0)
        neighbours = map[node]

        for next in neighbours:
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

    path.reverse()

    if path[0] == s:
        return path
    else:
        return 0


def get_shortest_path(map):
    prev = solve_search(get_starting_point())
    print(prev)
    return reconstructPath(get_starting_point(), get_highest_point(), prev)


print((get_shortest_path(map)))


def find_shortest_path(s, e):
    pass
