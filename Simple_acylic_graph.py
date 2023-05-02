import matplotlib.pyplot as plt
import networkx as nx

nodes = list(range(10))
names = ['Janssen', 'Janssen inc', 'Janssen thera', 'Janssen inc drugs', '4', '5', '6', '7', '8', '9']
edges = [(1, 0), (2, 1), (3, 2), (4, 1), (5, 0),
         (0, 5), (6, 3), (7, 3), (8, 0), (9, 8)]

gx = nx.DiGraph()
gx.add_nodes_from(nodes)
gx.add_edges_from(edges)


pr = nx.pagerank(gx, max_iter=1000)
print(pr)
#tada we made our graph
#Now lets plot it

pos = nx.spring_layout(gx)
nx.draw_networkx_nodes(gx, pos=pos, node_size=[pr[node]*300 for node in nodes])
nx.draw_networkx_edges(gx, pos=pos)
plt.show()

top_node_number = None
top_node_pagerank = -1
for node_number, pagerank in pr.items():
    if pagerank > top_node_pagerank