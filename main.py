# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt
#
# graph = nx.Graph()
# stop = 3
# for node in range(1, stop + 1):
#     graph.add_node(node)
#
# max_number = 2 * stop - 1
# num = 1
# squares = []
# while num ** 2 <= max_number:
#     squares.append(num ** 2)
#     num = num + 1
#
# for first in graph.nodes:
#     for second in graph.nodes:
#         if first < second:
#             summation = first + second
#             if summation in squares:
#                 graph.add_edge(first, second, label = str(summation))
#
# _, ax = plt.subplots()
# ax.set_title("Graph up to" + str(stop) + ".")
# pos = nx.circular_layout(graph)
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
# nx.draw_networkx_edges(
#     graph,
#     pos,
#     width=2,
#     alpha=0.5,
#     edge_color="black",
#
# )
# nx.draw_networkx_edge_labels(
#     graph,
#     pos,
#     nx.get_edge_attributes(graph, "label"),
#     font_size=12,
# )
#
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt


def comb(L):
    all = []
    for i in range(3):
        for j in range(3):
            for k in range(3):

                # check if the indexes are not
                # same
                all.append([L[i], L[j], L[k]])

    return all


def num_diff_let(a,b):
    u = zip(a, b)

    x = []
    diff = []
    for i, j in u:
        if i == j:
            continue
        else:
            x.append(j)
            diff = [a.index(i), b.index(j)]

    return x, diff


def graph_maker():
    rm = []
    nodes = comb([1, 2, 3])
    graph = nx.Graph()
    for node in nodes:
        name = f"{node[0]}{node[1]}{node[2]}"
        graph.add_node(name, room=1500)
    for first in graph.nodes:
        # print(first)
        for second in graph.nodes:
            diff, idx = num_diff_let(first, second)
            if len(diff) == 1:
                # if (first[0:-2] == second[0:-2]) or ((first[0] != second[1] and first[0] != second[2]) and first[1] != second[2]):

                if idx[0] == 2:
                    print(first, second, idx)
                    graph.add_edge(first, second)
                    rm.append((second, first))
                else:
                    print(idx)
                    test = True
                    ran1 = range(idx[0], 3)
                    ran2 = range(idx[1],3)
                    for index in ran1:
                        if first[idx[0]] == first[index]:
                            test = False
                    for index in ran2:
                        if first[idx[0]] == first[index]:
                            test = False
                    if test:
                        if first == "333":
                            print(first, second, idx)
                        if (first, second) not in rm:
                            graph.add_edge(first, second)
                            rm.append((second, first))

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