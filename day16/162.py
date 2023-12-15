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


def traveling_salesman(graph, current_node, visited, time_remaining):
    if not visited:
        visited = set()
    visited.add(current_node)

    if not graph[current_node]['connected_valves']:
        return 0

    min_cost = float('inf')

    for neighbor in graph[current_node]['connected_valves']:
        if neighbor not in visited:
            move_time = 1
            open_time = 1
            cost = move_time + open_time + traveling_salesman(
                graph,
                neighbor,
                visited.copy(),
                time_remaining - move_time - open_time,
            )
            min_cost = min(min_cost, cost)

    return min_cost


graph = {
    'AA': {'flow_rate': 0, 'connected_valves': ['DD', 'II', 'BB']},
    'BB': {'flow_rate': 13, 'connected_valves': ['CC', 'AA']},
    'CC': {'flow_rate': 2, 'connected_valves': ['DD', 'BB']},
    'DD': {'flow_rate': 20, 'connected_valves': ['CC', 'AA', 'EE']},
    'EE': {'flow_rate': 3, 'connected_valves': ['FF', 'DD']},
    'FF': {'flow_rate': 0, 'connected_valves': ['EE', 'GG']},
    'GG': {'flow_rate': 0, 'connected_valves': ['FF', 'HH']},
    'HH': {'flow_rate': 22, 'connected_valves': ['GG']},
    'II': {'flow_rate': 0, 'connected_valves': ['AA', 'JJ']},
    'JJ': {'flow_rate': 21, 'connected_valves': ['II']},
}

start_node = 'AA'
time_limit = 30

min_total_cost = traveling_salesman(graph, start_node, set(), time_limit)

print(f"Maximum gas flow in 30 minutes: {min_total_cost}")
