import matplotlib.pyplot as plt
import networkx as nx
import random

def give(graph,node_num) :
    neighbor_dict = graph[node_num]
    neighbor_list = graph.neighbors(node_num)
    nbers = len(neighbor_dict)
    nbersl = len(neighbor_list)
    money = graph.node[node_num]['value']
    print(money)
    print(nbers)
    print(nbersl)


G = nx.path_graph(3)
count = 0

# for node in G.nodes :
#     node[count]['value'] = random.randint(-1,1)
G.nodes[0]['value'] = -2
G.nodes[1]['value'] = -1
G.nodes[2]['value'] = 4

give(G,-1)

#print(G.nodes.data())
# nx.draw(G, with_labels=True)
# plt.show()