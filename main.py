import matplotlib.pyplot as plt
import networkx as nx
import random
from give import *

G = nx.path_graph(3)

G.nodes[0]['value'] = -2
G.nodes[1]['value'] = -1
G.nodes[2]['value'] = 4

# G = nx.Graph()
# G.add_edges_from([(-2, -1), (-1, 4)])

node_num = -1
while node_num != 'exit' :
    print(G.nodes)
    # nx.draw_networkx_labels(G,G.graph)
    nx.draw(G)

    # labels (dictionary, optional (default=None)) – Node labels in a dictionary keyed by node of text labels
    nx.draw_networkx(G,labels=G.nodes)
    plt.show()
    node_num = input('Which node do you want give money from?')

    give(G, int(node_num))
