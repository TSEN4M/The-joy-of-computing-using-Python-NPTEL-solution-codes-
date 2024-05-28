import networkx as nx
import random
import matplotlib.pyplot as plt
                         #adding edges to the nodes
                         
def add_edges(G):
     nodes=list(G.nodes())
     for s in nodes:
          for t in nodes:
               if s!=t:
                    r=random.random()
                    if r<=0.5:
                         G.add_edge(s,t)
     return G

def assign_points(G):
     nodes=list(G.nodes())
     p=[]
     for each in nodes:
          p.append(100)
     return p

def keep_distributing(G,points):
     while(1):
          new_points=distribute_points(G,points)
          print(new_points)
          points=new_points
          stop=input('press # to stop or any other key to continue : ')
          if stop=='#':
               break
     return new_points

def distribute_points(G,points):
     nodes=list(G.nodes())
     new_points=[]
     for i in range(len(nodes)):
          new_points.append(0)
          
     for n in nodes:
          out=list(G.out_edges(n))       #checking for outgoing edges      
          if len(out)==0:
               new_points[n]=new_points[n]+points[n]
          else:
               share=points[n]/len(out)      #if edge is present the points is given as per directed to by share value
               for (src,tgt) in out:
                    new_points[tgt]=new_points[tgt]+share
     return new_points               
                    
def rank_by_points(points):  #final point is a list
     #converting a list to a dictionary structure and then sort 
     d={}
     for i in range(len(points)):
          d[i]=points[i]
     print(sorted(d.items(),key=lambda f:f[1]))            #sorted() has argument 1st for what to sort and 2nd(key) for based on what to sort
                    
G=nx.DiGraph()

G.add_nodes_from(i for i in range(10))       #creating directed graph
G=add_edges(G)

                              #visulizing the graph
nx.draw(G,with_labels=True)
plt.show()
                              #assingn initial points
points=assign_points(G)

                              #keep distributing
final_points=keep_distributing(G,points)

                              #rank by points
rank_by_points(final_points)

#default networkx function for pagerank return a dictionary 
result=nx.pagerank(G)
print('using networkx :',sorted(result.items(),key=lambda f:f[1]))
