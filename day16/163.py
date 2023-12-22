import re
with open("day16/ex.txt", "r") as file:
    file_contents = file.read()

graph = {}

for line in file_contents.strip().split('\n'):
    match = re.match(
        r'Valve (\w+) has flow rate=(\d+); tunnels lead to valves (.+)', line
    )
    match2 = re.match(
        r'Valve (\w+) has flow rate=(\d+); tunnel leads to valve (.+)', line
    )
    if match:
        current_valve, flow_rate, connected_valves = match.groups()
        graph[current_valve] = {
            "flow_rate": int(flow_rate),
            "connected_valves": connected_valves.split(", "),
        }
    elif match2:
        current_valve, flow_rate, connected_valves = match2.groups()
        graph[current_valve] = {
            "flow_rate": int(flow_rate),
            "connected_valves": connected_valves.split(", "),

        }


def solve_search(start_node, graph):
    queue = []
    queue.append(start_node)
    visited = {node: False for node in graph}
    visited[start_node] = True
    previous = {node: None for node in graph}
    while queue:

        current_node = queue.pop(0)
        neighbors = graph[current_node]["connected_valves"]
        for next_node in neighbors:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                previous[next_node] = current_node
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


def find_distances(graph):
    distances = {}
    for s in graph:
        if graph[s]["flow_rate"] > 0 or s == "AA":
            distances[s] = {}
            search = solve_search(s, graph)
            for e in graph:
                distances[s][e] = (reconstructPath(s, e,  search))

    return distances


def find_valves(graph):
    valves = []
    for s in graph:
        if graph[s]["flow_rate"] > 0 or s == "AA":
            valves.append(s)
    return valves


def find_rates(distances, valve, minutes, left, opened={}):

    all_rates = [opened]

    for i, item in enumerate(left):
        print(item)
        print(distances)
        print(distances[valve][item])
        minutes_left = minutes - distances[valve][item] - 1
        if minutes_left < 1:
            return

        new_opened = opened
        new_opened[item] = minutes_left

        new_left = left
        new_left.remove(item)
        all_rates.append(find_rates(distances, item,
                         minutes_left, new_left, new_opened))

    return all_rates


distances = find_distances(graph)
filtered_valves = find_valves(graph)

rates = find_rates(distances, "AA", 30, find_valves(graph))

print(len(rates))
