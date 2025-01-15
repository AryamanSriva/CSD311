import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

for i in range(3):
    for j in range(3):
        G.add_node((i, j))

edges = [
    ((0, 1), (0, 2)),
    ((1, 0), (1, 1)),
    ((1, 1), (1, 2)),
    ((2, 0), (2, 1)),
    ((2, 0), (1, 0)),
    ((1, 0), (1, 1)),
    ((1, 1), (0, 1)),
    ((1, 2), (0, 2)),
    ((1, 0), (1, 1)),
    ((2, 1), (1, 1))
]
G.add_edges_from(edges)

plt.figure(figsize=(10, 10))

node_colors = {
    (0, 0): 'gray',
    (0, 1): 'skyblue',
    (0, 2): 'red',
    (1, 0): 'skyblue',
    (1, 1): 'skyblue',
    (1, 2): 'skyblue',
    (2, 0): 'green',
    (2, 1): 'skyblue',
    (2, 2): 'gray'
}

colors = [node_colors[node] for node in G.nodes()]

pos = {(x, y): (y, -x) for x, y in G.nodes()}
nx.draw(G, pos, node_color=colors, node_size=3000, arrowsize=20, with_labels=True)

labels = {node: str(node) for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=12)

plt.axis('off')
plt.tight_layout()
plt.show()