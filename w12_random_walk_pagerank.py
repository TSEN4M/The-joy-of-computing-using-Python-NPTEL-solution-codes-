import networkx as nx
import random
import matplotlib.pyplot as plt
import operator

G=nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)   #literal set to true
plt.show()
          #x is a random source node
x=random.choice([i for i in range(G.number_of_nodes())])    #can be replaced by nx.number_of_nodes(G)

dict_counter={}          
for i in range(G.number_of_nodes()):
     dict_counter[i]=0
     
dict_counter[x]=dict_counter[x]+1       #counts the number of visits to the node

for i in range(100):
     list_n=list(G.neighbors(x))
     
     if len(list_n)==0:       #if x is a sink
          x=random.choice([i for i in range(G.number_of_nodes())])
          dict_counter[x]=dict_counter[x]+1
     else:
          x=random.choice(list_n)       #choose a node randomly from neighbor of x
          dict_counter[x]=dict_counter[x]+1

p=nx.pagerank(G)         #functions for finding pagerank 
sorted_p=sorted(p.items(),key=operator.itemgetter(1))       #1 for value and 0 for key sorting in dictionary
sorted_rw=sorted(dict_counter.items(),key=operator.itemgetter(1))
print('p value is : ',sorted_p)
print('random walk value : ',sorted_rw)