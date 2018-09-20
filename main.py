import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import networkx as nx
import random
from give import *

style.use('fivethirtyeight')

G = nx.path_graph(3)

G.nodes[0]['value'] = -2
G.nodes[1]['value'] = -1
G.nodes[2]['value'] = 4

# G = nx.Graph()
# G.add_edges_from([(-2, -1), (-1, 4)])
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i, G) :
    ax1.clear()
    nx.draw_networkx(G,labels=G.nodes)
    ax1.plot()

node_num = -1
# plt.ion()
# nx.draw_networkx(G,labels=G.nodes)
# plt.cla()
while node_num != 'exit' :
    ani = animation.FuncAnimation(fig,animate, interval=1000)
    node_num = input('Which node do you want give money from?')
    give(G, int(node_num))