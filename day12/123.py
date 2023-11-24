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


def get_shortest_path(map):
    start = get_starting_point()
    frontier = [start]
    explored = [start]

    while len(frontier) > 0:
        path = {}
        current_cell = frontier.pop(0)

        if current_cell == (20, 56):
            print("holaaa")
            break

        for direction in 'NESW':

            if map[current_cell][direction] == True:
                if direction == 'E':
                    child_cell = (current_cell[0], current_cell[1]+1)
                if direction == 'W':
                    child_cell = (current_cell[0], current_cell[1]-1)
                if direction == "N":
                    child_cell = (current_cell[0]-1, current_cell[1])
                if direction == "S":
                    child_cell = (current_cell[0]+1, current_cell[1])

                if child_cell in explored:
                    continue
                frontier.append(child_cell)
                explored.append(child_cell)
                path[child_cell] = current_cell

    forward_path = {}
    cell = get_starting_point()
    while cell != start:
        forward_path[path[cell]] = cell
        cell = path[cell]
    return forward_path


map = set_up_graph(contents)
print(len(get_shortest_path(map)))
