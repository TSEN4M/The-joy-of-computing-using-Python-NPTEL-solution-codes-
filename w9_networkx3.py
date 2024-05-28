import networkx as nx
import matplotlib.pyplot as plt

#G=nx.gnp_random_graph(50,0.3)

#scale free graph
G=nx.barabasi_albert_graph(50,2)        #50=no of nodes 2=each node is coming out with 2 new edges
print(G.edges())
print(G.degree(0))

nx.draw(G)
plt.show()

nx.write_gexf(G,'nx_analysis.gexf')