import networkx as nx
import matplotlib.pyplot as plt
from itertools import product
import re


class HanoiTower:
    def __init__(self, disks, towers, start, end):
        self.disks = disks
        self.towers = towers
        self.nums = []
        self.disk_names = self.disk_names()
        self.nodes = product(self.nums, repeat=len(self.disk_names))
        self.graph = nx.Graph()
        self.start = start
        self.end = end
        self.diff = []
        self.idx = []
        self.node_color_map = []
        self.edge_color_map = []
        self.edge_width = []
        self.short_path_edges = []
        self.short_path_nodes = []

    def disk_names(self):
        names = ''.join(map(str, list(range(1, self.disks + 1))))
        self.nums = ''.join(map(str, list(range(1, self.towers + 1))))
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

    def find_shortest_path(self):
        self.short_path_nodes = nx.shortest_path(self.graph, self.start, self.end)
        i = 0
        while i < len(self.short_path_nodes)-1:
            if i == 0:
                self.short_path_edges.append(('start', self.short_path_nodes[i + 1]))
                self.short_path_edges.append((self.short_path_nodes[i + 1], 'start'))
            elif i == len(self.short_path_nodes)-2:
                self.short_path_edges.append((self.short_path_nodes[i], 'end'))
                self.short_path_edges.append(('end', self.short_path_nodes[i]))
            else:
                self.short_path_edges.append((self.short_path_nodes[i], self.short_path_nodes[i + 1]))
                self.short_path_edges.append((self.short_path_nodes[i+1], self.short_path_nodes[i]))
            i += 1
        for node in self.short_path_nodes:
            if node == self.end:
                self.node_color_map.append('red')
                self.short_path_nodes[-1] = 'end'
            elif node == self.start:
                self.node_color_map.append('green')
                self.short_path_nodes[0] = 'start'
            elif node in self.short_path_nodes:
                self.node_color_map.append('orange')

        for edge in self.graph.edges:
            if edge in self.short_path_edges:
                self.edge_color_map.append("green")
        self.graph = nx.relabel_nodes(self.graph, {self.start: 'start', self.end: 'end'})
        self.plot_tower()

    def plot_tower(self):
        iter_graph = 10000
        size = 400
        if self.disks == 6:
            fig = plt.figure(1, figsize=(50, 50), dpi=60)
            size = 700
            iter_graph = 100
        pos = nx.spring_layout(self.graph, iterations=iter_graph)
        nx.draw_networkx_labels(
            self.graph,
            pos,
            font_size=8,
            font_family="sans-serif",
        )
        nx.draw(self.graph, pos, with_labels=False, node_color="grey", edge_color="grey", node_size=size)
        nx.draw(self.graph, pos, nodelist=self.short_path_nodes, node_color=self.node_color_map,
                edgelist=self.short_path_edges, edge_color="green", width=3, node_size=size)
        plt.show()


# test = HanoiTower(6, 3, '111111', '333333')
test = HanoiTower(3, 3, '111', '333')
test.create_tower()
