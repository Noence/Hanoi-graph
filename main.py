import networkx as nx
import matplotlib.pyplot as plt
from itertools import product
import re


class HanoiTower:
    def __init__(self, disks, towers):
        self.disks = disks
        self.towers = towers
        self.disk_names = self.disk_names()
        self.nodes = product(self.disk_names, repeat=self.towers)
        self.graph = nx.Graph()
        self.diff = []
        self.idx = []

    def disk_names(self):
        names = ''.join(map(str, list(range(1, self.disks + 1))))
        return names

    def num_diff_let(self, a, b):
        u = zip(a, b)

        self.diff = []
        self.idx = []
        for i, j in u:
            if i == j:
                continue
            else:
                self.diff.append(j)
                self.idx = [a.index(i), b.index(j)]

    def create_tower(self):
        for node in self.nodes:
            self.graph.add_node(''.join(node), room=1500)
        for first in self.graph.nodes:
            for second in self.graph.nodes:
                self.num_diff_let(first, second)
                if len(self.diff) == 1:
                    first_lst = re.findall(".", first)
                    second_lst = re.findall(".", second)

                    if self.idx[0] == 2:
                        self.graph.add_edge(first, second)
                    else:
                        i = 0
                        for num in first_lst:
                            if (num not in (first_lst[i + 1:])) and (second[i] != num) and (
                                    second[i] not in (second_lst[i + 1:])):
                                self.graph.add_edge(first, second)
                            i += 1
        self.plot_tower()

    def plot_tower(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True)
        plt.show()


# graph_maker(3,3)
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


test = HanoiTower(3, 3)
test.create_tower()
