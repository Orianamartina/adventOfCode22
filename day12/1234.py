with open("day12/12input.txt", "r") as file:
    file_contents = file.read()


contents = file_contents.split("\n")
map_height = len(contents)
map_width = len(contents[0])

# global
item_heights = "SabcdefghijklmnopqrstuvwxyzE"


def set_up_graph(contents):

    graph = []
    counter = 0
    for i in range(map_height):
        for j in range(map_width):
            graph.append([])
            if j > 0:
                if item_heights.index(contents[i][j-1]) == item_heights.index(contents[i][j]) or item_heights.index(contents[i][j-1]) == item_heights.index(contents[i][j])+1:
                    graph[counter].append(counter-1)
            if j < map_width - 1:
                if item_heights.index(contents[i][j+1]) == item_heights.index(contents[i][j]) or item_heights.index(contents[i][j+1]) == item_heights.index(contents[i][j])+1:
                    graph[counter].append(counter+1)
            if i > 0:
                if item_heights.index(contents[i-1][j]) == item_heights.index(contents[i][j]) or item_heights.index(contents[i-1][j]) == item_heights.index(contents[i][j])+1:
                    graph[counter].append(counter - map_width)
            if i < map_height - 1:
                if item_heights.index(contents[i+1][j]) == item_heights.index(contents[i][j]) or item_heights.index(contents[i+1][j]) == item_heights.index(contents[i][j])+1:
                    graph[counter].append(counter + map_width)
            if (i, j) == (20, 0):
                graph[counter].append(counter + 1)
            counter += 1
    return graph


visited = []
queue = []


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


def get_shortest_path(visited, graph, node):
    visited.append(node)
    queue.append(node)
    path = {}
    while queue:
        m = queue.pop(0)
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
            path[neighbor] = graph[m]

    short = []
    print(path)
    current = get_highest_point()
    while current != get_starting_point():
        short.append(current)

        current = path[current]

    return short


def reconstructPath(s, e, previous):
    path = []
    at = e
    while at is not None:
        path.append(at)
        at = previous[at]
        print(path)

    path = path.reverse()
    if path[0] == s:
        return path
    else:
        return 0


map = set_up_graph(contents)
print(get_starting_point())
get_shortest_path(visited, map, get_starting_point())
