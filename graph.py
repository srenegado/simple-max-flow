# graph.py
# Simple graph implementation as an adjacency list.
# (https://en.wikipedia.org/wiki/Adjacency_list)
# Scott Renegado

class Graph:
    """
    Simple flow network implementation as an adjacency list.
    E.g. node1 is adjacent to node2 with 0 flow and 10 capacity:
    node1: [node2, 10, 0]
    """
    def __init__(self, n):
        self.n = n
        self.nodes = range(self.n)
        self.adj_list = {}
        for node in self.nodes:
            self.adj_list[node] = []

    def print_adj_list(self):
        for node,adj in self.adj_list.items():
            print(f"node {node}: {adj}")

    def add_edge(self, node1, node2, capacity=0, flow=0):
        self.adj_list[node1].append([node2, capacity, flow])

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(*edge)

    def size_n(self):
        return self.n

    def get_adj_list(self):
        return self.adj_list

    def get_adjacencies(self, node):
        return self.adj_list.get(node, [])

    def augment_flow(self, node1, node2, aug):
        for adj in self.get_adj_list().get(node1, []):
            if adj[0] == node2:
                adj[2] = adj[2] + aug