import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
nodes=[1,2,3]
edges=[[1,2],[2,3],[1,3]]

G.add_nodes_from(nodes)  
                              #adding the nodes and edges from a list
G.add_edges_from(edges)

H=nx.complete_graph(10)           #creating a complete graph of 10 nodes

I=nx.gnp_random_graph(20,0.1)      #creating a random graph with 20 nodes and edge probability within them is 0.1

nx.draw(I)               #drawing the graph I

plt.show()               #printing the recently created graph