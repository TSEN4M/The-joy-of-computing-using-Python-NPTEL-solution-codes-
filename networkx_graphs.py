import networkx as nx
import matplotlib.pyplot as plt

a=4
b=3
G=nx.barbell_graph(a,b)  #draws two seperated communities of a nodes and b seperation nodes
plt.title('BARBELL GRAPH')
nx.draw(G)
plt.show()

C=nx.complete_graph(4) #4 is the number of nodes
plt.title('COMPLETE GRAPH')
nx.draw(C)
plt.show()

CY=nx.cycle_graph(5)
plt.title('CYCLE GRAPH')
nx.draw(CY)
plt.show()

LA=nx.ladder_graph(5)
plt.title('LADDER GRAPH')
nx.draw(LA)
plt.show()

PA=nx.path_graph(6)
plt.title('PATH GRAPH')
nx.draw(PA)
plt.show()

S=nx.star_graph(5)
plt.title('STAR GRAPH')
nx.draw(S)
plt.show()

W=nx.wheel_graph(6)
plt.title('WHEEL GRAPH')
nx.draw(W)
plt.show()

R=nx.gnp_random_graph(5,0.5)
plt.title('RANDOM GRAPH')
nx.draw(R)
plt.show()
