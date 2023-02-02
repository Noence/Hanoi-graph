import networkx as nx
import matplotlib.pyplot as plt
from itertools import product
import re

def num_diff_let(a, b):
    u = zip(a, b)

    diff = []
    idx = []
    for i, j in u:
        if i == j:
            continue
        else:
            diff.append(j)
            idx = [a.index(i), b.index(j)]

    return diff, idx


def graph_maker():
    rm = []
    nodes = product('123', repeat=3)
    graph = nx.Graph()
    for node in nodes:
        name = f"{node[0]}{node[1]}{node[2]}"
        graph.add_node(name, room=1500)
    for first in graph.nodes:
        for second in graph.nodes:
            diff, idx = num_diff_let(first, second)
            if len(diff) == 1:
                first_lst = re.findall(".", first)
                second_lst = re.findall(".", second)

                if idx[0] == 2:
                    graph.add_edge(first, second)
                    rm.append((second, first))
                else:
                    i = 0
                    for num in first_lst:
                        if (num not in (first_lst[i + 1:])) and (second[i] != num) and (second[i] not in (second_lst[i + 1:])):
                            graph.add_edge(first, second)
                            rm.append((second, first))
                        i += 1


    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.show()

graph_maker()
# nx.draw_networkx_nodes(
#     graph,
#     pos,
#     node_size=500,
#     node_color="white",
#     linewidths=1,
#     edgecolors="black",
#
# )
# nx.draw_networkx_labels(
#     graph,
#     pos,
#     font_size=16,
#     font_family="sans-serif",
# )
# nx.draw(graph, pos, with_labels=True)
# plt.show()
