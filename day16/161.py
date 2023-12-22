import re
with open("day16/16input.txt", "r") as file:
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


def sort_graph_by_flow_rate(graph):
    filtered_graph = {key: value for key,
                      value in graph.items() if value['flow_rate'] != 0}
    sorted_graph = sorted(filtered_graph.items(),
                          key=lambda x: x[1]['flow_rate'], reverse=True)
    return sorted_graph


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


def get_next_node(data, minutes_left):
    # data: {flow_rate: distance}
    rates = []
    for node in data:
        flow, distance = next(iter(node.items()))
        rates.append(flow * (minutes_left - distance + 1))
    return (rates.index(max(rates)))


mins = 0
i = 0
total_pressure_release = 0
current_valve = "AA"
while mins < 30:
    print("Current valve: ", current_valve)
    total_path = solve_search(current_valve, graph)
    sorted_valves = sort_graph_by_flow_rate(graph)
    print(sorted_valves)
    possible_valves = []
    for valve in sorted_valves:

        graph_valve = graph[valve[0]]
        possible_valves.append({graph_valve["flow_rate"]: reconstructPath(
            current_valve, valve[0], total_path)})
        # el indice de esto es el mismo que el indice en sorted valves
    if possible_valves:
        closest_valve = get_next_node(possible_valves, mins)
        current_valve = sorted_valves[closest_valve]
        time_spent = next(iter(possible_valves[closest_valve].values()))
        mins += time_spent + 1
        total_pressure_release += (30 - mins) * \
            sorted_valves[closest_valve][1]["flow_rate"]
        graph[sorted_valves[closest_valve][0]]["flow_rate"] = 0
        current_valve = current_valve[0]
    else:
        mins = 30
print(total_pressure_release)
