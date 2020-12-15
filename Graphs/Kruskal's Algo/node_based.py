import sys
class Vertex:
    def __init__(self,k):
        self.id = k
        self.color = 'white'
        self.distance=sys.maxsize
        self.connectedTo = {}
        self.Pred = None
        self.next = None
    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def setDistance(self,dist):
        self.distance = dist
    def getDistance(self):
        return self.distance
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def setPred(self,node):
        self.Pred = node
    def getPred(self):
        return self.Pred
    def getNext(self):
        return self.next
    def setNext(self,nxt):
        self.next = nxt

    def __str__(self):
        return "ID:" + str(self.id) + "Value: " + str(self.distance) + " Color:" + str(self.color) + "ConnectedTo\n" + \
               f"{[(i.id) for i in self.connectedTo]}"


class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self,key):
        if key not in self.graph:
            nv = Vertex(key)
            self.graph[key] = nv
            return nv
        else:
            return None
    def addEdge(self,f,t,cost=0):
        if f not in self.graph:
            nv1 = Vertex(f)
            self.graph[f] = nv1
        if t not in self.graph:
            nv2 = Vertex(t)
            self.graph[t] = nv2
        self.graph[f].addNeigh(self.graph[t],cost)
    def getVertex(self,key):
        return self.graph[key]
    def __iter__(self):
        return iter(self.graph.values())

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
            print(elem_ref.key.id,elem_ref.parent.key.id)
            elem_ref.parent = self.find_set(elem_ref.parent.key)
            print(elem_ref.parent.key.id)
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



g = Graph()
g.addEdge(0,1,1)
g.addEdge(1,0,1)
g.addEdge(1,2,2)
g.addEdge(2,1,2)
g.addEdge(0,2,3)
g.addEdge(2,0,3)
g.addEdge(1,3,3)
g.addEdge(3,1,3)

edges = []
seen = set()
num_nodes =0
for i in g:
    num_nodes+=1
    for j in i.getConnections():
        if((i,j) not in seen):
            seen.add((j,i))
            edges.append((i,j,i.getWeight(j)))
#print(edges)
edges.sort(key=lambda edge:edge[2])
disjoint_set = DisjointSetTree()
[disjoint_set.make_set(i) for i in g]

num_edges =0
sum=0
index = 0
final_graph = Graph()
while num_edges<num_nodes-1:
    u,v,w = edges[index]
    index +=1
    print(u.id,v.id)
    parentu = disjoint_set.find_set(u)
    parentv = disjoint_set.find_set(v)
    if parentu != parentv:
        num_edges += 1
        sum+=w
        final_graph.addEdge(u, v, w)
        disjoint_set.union(u, v)
