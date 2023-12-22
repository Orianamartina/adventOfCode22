from functools import cache
import re
with open("day16/16input.txt", "r") as file:
    file_contents = file.read()

graph = {}
flows = {}


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
        flows[current_valve] = int(flow_rate)
    elif match2:
        current_valve, flow_rate, connected_valves = match2.groups()
        graph[current_valve] = {
            "flow_rate": int(flow_rate),
            "connected_valves": connected_valves.split(", "),

        }
        flows[current_valve] = int(flow_rate)


@cache
def solve(position, time, opened_valves, e=False):
    if time == 0:
        if e:
            return solve("AA", 26, opened_valves)
        return time
    # hijos

    score = max(solve(n, time - 1, opened_valves, e)
                for n in graph[position]["connected_valves"])
    # Actual si su flow_rate es mayor a 0 y no fue abierta previamente
    if flows[position] > 0 and position not in opened_valves:
        new_opened = set(opened_valves)
        new_opened.add(position)
        # Se suman los flowrate, se compara
        score = max(
            score,
            (time - 1) * flows[position]
            + solve(position, time - 1, frozenset(new_opened), e),
        )
    return score


print(solve("AA", 30, frozenset()))
print(solve("AA", 26, frozenset(), True))
