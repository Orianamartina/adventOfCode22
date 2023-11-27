import collections

with open("day12/12input.txt", "r") as file:
    file_contents = file.read()


contents = file_contents.split("\n")
map_height = len(contents)
map_width = len(contents[0])

# global
item_heights = "SabcdefghijklmnopqrstuvwxyzE"


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


def set_up_graph(contents):

    graph = {}
    counter = 0
    for i in range(map_height):
        for j in range(map_width):
            graph[counter] = []
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
    print(graph[1656])
    return graph


class Graph():
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return not self.elements

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def breadth_first_search(graph, start):
    frontier = Queue()
    frontier.put(start)

    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        for next_node in graph.neighbors(current):
            if next_node not in came_from:
                frontier.put(next_node)
                came_from[next_node] = current
    return came_from


def explore_all_nodes(graph):
    all_nodes = set(graph.edges)
    visited_nodes = set()

    components = []
    for node in all_nodes:
        if node not in visited_nodes:
            component = breadth_first_search(graph, node)
            visited_nodes.update(component.keys())
            components.append(component)

    return components


def reconstructPath(s, e, previous):
    path = []
    at = e
    while at is not None:
        path.append(at)
        at = previous[at]
    path = path[::-1]
    if path[0] == s:
        return len(path)
    else:
        return 0


graph = Graph()
graph.edges = set_up_graph(contents)
explore_all_nodes(graph)
print(reconstructPath(get_starting_point(),
                      get_highest_point(), explore_all_nodes(graph)[27]))


bfs = breadth_first_search(graph, get_starting_point())
