import matplotlib.pyplot as plt
import networkx as nx
import re
with open("day16/ex.txt", "r") as file:
    file_contents = file.read()

input_data = file_contents


# Create a directed graph
G = nx.DiGraph()

# Parse input data and add nodes and edges to the graph
for line in input_data.strip().split('\n'):
    match = re.match(
        r'Valve (\w+) has flow rate=(\d+); tunnels lead to valves (.+)', line)
    if match:
        current_valve, flow_rate, connected_valves = match.groups()
        G.add_node(current_valve, flow_rate=int(flow_rate))
        connected_valves = connected_valves.split(', ')
        for connected_valve in connected_valves:
            G.add_edge(current_valve, connected_valve)

# Print graph nodes and edges
print("Nodes:", G.nodes())
print("Edges:", G.edges())

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700,
        node_color='skyblue', font_size=8, edge_color='gray')
labels = nx.get_edge_attributes(G, 'flow_rate')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
