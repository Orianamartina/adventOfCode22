with open("day12/12input.txt", "r") as file:
    file_contents = file.read()

from queue import PriorityQueue

"""
there could be various path alternatives to follow
we need the shortest one 
"""

contents = file_contents.split("\n")
map_height = len(contents)
map_width = len(contents[0])

# global
item_heights = "SabcdefghijklmnopqrstuvwxyzE"

all_positions = []


def set_up_graph(contents):

    graph = {}
    for i in range(map_height):
        for j in range(map_width):
            all_positions.append((i, j))
            graph[(i, j)] = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

            if j > 0:
                if item_heights.index(contents[i][j-1]) == item_heights.index(contents[i][j]) or item_heights.index(contents[i][j-1]) == item_heights.index(contents[i][j])+1:
                    graph[i, j]["W"] = 1
            if j < map_width - 1:
                if item_heights.index(contents[i][j+1]) == item_heights.index(contents[i][j]) or item_heights.index(contents[i][j+1]) == item_heights.index(contents[i][j])+1:
                    graph[i, j]["E"] = 1
            if i > 0:
                if item_heights.index(contents[i-1][j]) == item_heights.index(contents[i][j]) or item_heights.index(contents[i-1][j]) == item_heights.index(contents[i][j])+1:
                    graph[i, j]["N"] = 1
            if i < map_height - 1:
                if item_heights.index(contents[i+1][j]) == item_heights.index(contents[i][j]) or item_heights.index(contents[i+1][j]) == item_heights.index(contents[i][j])+1:
                    graph[i, j]["S"] = 1
            if (i, j) == (20, 0):
                graph[i, j]["E"] = 1
    return graph


def get_starting_point():
    for i in range(map_height):
        for j in range(map_width):
            if contents[i][j] == "S":
                return ((i, j))


def get_highest_point():
    for i in range(map_height):
        for j in range(map_width):
            if contents[i][j] == "E":
                return ((i, j))


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1-x2) + abs(y1-y2)


def get_shortest_path(map):

    start = get_starting_point()
    goal = get_highest_point()
    g_score = {cell: float('inf') for cell in all_positions}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in all_positions}
    # f_cost = heuristic cost(h) + g_cost
    f_score[start] = h(start, goal)

    queue = PriorityQueue()
    # f_cost
    queue.put((h(start, goal), h(start, goal), start))

    path = {}
    while not queue.empty():
        # cell value
        current_cell = queue.get()[2]
        if current_cell == goal:
            print("wenaas")
            forward_path = {}
            cell = goal
            while cell != start:
                forward_path[path[cell]] = cell
                cell = path[cell]

            return forward_path
        for direction in 'NESW':
            if map[current_cell][direction]:
                if direction == 'E':
                    child_cell = (current_cell[0], current_cell[1]+1)
                if direction == 'W':
                    child_cell = (current_cell[0], current_cell[1]-1)
                if direction == "N":
                    child_cell = (current_cell[0]-1, current_cell[1])
                if direction == "S":
                    child_cell = (current_cell[0]+1, current_cell[1])
                temp_g_score = g_score[current_cell] + 1
                temp_f_score = temp_g_score + h(child_cell, goal)

                if temp_f_score < f_score[child_cell]:
                    g_score[child_cell] = temp_g_score
                    f_score[child_cell] = temp_f_score
                    queue.put(
                        (temp_f_score, h(child_cell, goal), child_cell))
                    path[child_cell] = current_cell

    forward_path = {}

    cell = goal

    while cell != start:
        forward_path[path[cell]] = cell
        cell = path[cell]

    return forward_path


map = set_up_graph(contents)
print(len(get_shortest_path(map)))
