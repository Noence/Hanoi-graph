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
        print(list(self.nodes))
        self.graph = nx.Graph()
        self.diff = []
        self.idx = []
        self.node_color_map = []
        self.edge_color_map = []


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
                    first_lst = re.findall('.', first)
                    second_lst = re.findall('.', second)

                    i = 0
                    for num in first_lst:
                        if (num not in (first_lst[i + 1:])) and (second[i] != num) and (
                                second[i] not in (second_lst[i + 1:])):
                            self.graph.add_edge(first, second)
                        i += 1
        self.find_shortest_path()
        self.plot_tower()

    def find_shortest_path(self):
        short_path_nodes = nx.shortest_path(self.graph, '111', '333')
        i = 0
        short_path_edges = []
        while i < len(short_path_nodes)-1:
            short_path_edges.append((short_path_nodes[i], short_path_nodes[i + 1]))
            short_path_edges.append((short_path_nodes[i+1], short_path_nodes[i]))
            i += 1
        for node in self.graph:
            if node in short_path_nodes:
                self.node_color_map.append('green')
            else:
                self.node_color_map.append('grey')
        for edge in self.graph.edges:
            if edge in short_path_edges:
                self.edge_color_map.append("green")
            else:
                self.edge_color_map.append('grey')

    def plot_tower(self):
        pos = nx.spring_layout(self.graph)
        # nx.draw_networkx_nodes(
        #     self.graph,
        #     pos,
        #     node_size=500,
        #     node_color="white",
        #     linewidths=1,
        #     edgecolors="black",
        #
        # )
        # nx.draw_networkx_labels(
        #     self.graph,
        #     pos,
        #     font_size=16,
        #     font_family="sans-serif",
        # )
        nx.draw(self.graph, pos, node_color=self.node_color_map, edge_color=self.edge_color_map, with_labels=True)
        plt.show()


test = HanoiTower(5, 3)
test.create_tower()
