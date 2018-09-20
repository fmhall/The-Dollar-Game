import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import networkx as nx
import random
from give import *
from get_node import *

G = nx.path_graph(3)

G.nodes[0]['value'] = -2
G.nodes[1]['value'] = -1
G.nodes[2]['value'] = 4

plt.ion()

while 1 :
    plt.clf()
    plt.gca(xmargin=.5,ymargin=.5)
    #pos = nx.bipartite_layout(G, )
    # nx.draw_networkx(G, pos=circular_layout(G), labels=G.nodes)
    nx.draw(G, with_labels=True, labels=G.nodes, node_size=1500, node_color="skyblue", pos=nx.fruchterman_reingold_layout(G))
    plt.show()
    node_num = get_node(G)
    give(G, int(node_num))