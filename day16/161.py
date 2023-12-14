import re

with open("day16/ex.txt", "r") as file:
    file_contents = file.read()

graph = {}

for line in file_contents.strip().split('\n'):
    match = re.match(
        r'Valve (\w+) has flow rate=(\d+); tunnels lead to valves (.+)', line)
    if match:
        current_valve, flow_rate, connected_valves = match.groups()
        graph[current_valve] = {
            "flow_rate": int(flow_rate),
            "connected_valves": connected_valves.split(", "),
        }


sorted_valves = sorted(graph.items(), key=lambda x: x[1]['flow_rate'], reverse=True)

def amount_of_time_to_get_to(valve):
    pass

mins = 0
i = 0
total_pressure_release = 0
while mins <= 30:
    if amount_of_time_to_get_to(sorted_valves[i][0]) < 30:
        i+=1
        total_pressure_release += sorted_valves[i][0]
    else:
        print(i) 

    