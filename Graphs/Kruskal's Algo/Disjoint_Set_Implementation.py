from __future__ import annotations


class DisjointSetTreeNode:
    # Disjoint Set Node to store the parent and rank
    def __init__(self, key: int) -> None:
        self.key = key
        self.parent = self
        self.rank = 0


class DisjointSetTree:
    # Disjoint Set DataStructure
    def __init__(self):
        # map from node name to the node object
        self.map = {}

    def make_set(self, x: int) -> None:
        # create a new set with x as its member
        self.map[x] = DisjointSetTreeNode(x)

    def find_set(self, x: int) -> DisjointSetTreeNode:
        # find the set x belongs to (with path-compression)
        elem_ref = self.map[x]
        if elem_ref != elem_ref.parent:
            elem_ref.parent = self.find_set(elem_ref.parent.key)
        return elem_ref.parent

    def link(self, x: int, y: int) -> None:
        # helper function for union operation
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1

    def union(self, x: int, y: int) -> None:
        # merge 2 disjoint sets
        self.link(self.find_set(x), self.find_set(y))


class GraphUndirectedWeighted:
    def __init__(self):
        # connections: map from the node to the neighbouring nodes (with weights)
        self.connections = {}

    def add_node(self, node: int) -> None:
        # add a node ONLY if its not present in the graph
        if node not in self.connections:
            self.connections[node] = {}

    def add_edge(self, node1: int, node2: int, weight: int) -> None:
        # add an edge with the given weight
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1][node2] = weight
        self.connections[node2][node1] = weight

    def kruskal(self) -> GraphUndirectedWeighted:

        # getting the edges in ascending order of weights
        edges = []
        seen = set()
        for start in self.connections:
            for end in self.connections[start]:
                if (start, end) not in seen:
                    seen.add((end, start))
                    edges.append((start, end, self.connections[start][end]))
        edges.sort(key=lambda x: x[2])
        print(edges)
        # creating the disjoint set
        disjoint_set = DisjointSetTree()
        [disjoint_set.make_set(node) for node in self.connections]
        # MST generation
        num_edges = 0
        index = 0
        graph = GraphUndirectedWeighted()
        while num_edges < len(self.connections) - 1:
            u, v, w = edges[index]
            index += 1
            parentu = disjoint_set.find_set(u)
            parentv = disjoint_set.find_set(v)
            if parentu != parentv:
                num_edges += 1
                graph.add_edge(u, v, w)
                print(u,v,w)
                disjoint_set.union(u, v)

        return graph

g = GraphUndirectedWeighted()
g.add_edge(0,1,1)
g.add_edge(1,2,2)
g.add_edge(2,0,3)
g.add_edge(1,3,4)

mst = g.kruskal()
