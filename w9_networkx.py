import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()   #graph is created but no edges and nodes are present

G.add_node(1)
G.add_node(2)       #node is created
G.add_node(3)

G.add_edge(1,2)
G.add_edge(2,3)     #edge is created
G.add_edge(1,3)

print(G.nodes)
print(G.edges)

nx.draw(G)
plt.show()