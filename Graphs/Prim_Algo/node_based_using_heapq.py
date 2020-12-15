import heapq

import sys
class Vertex:
    def __init__(self,k):
        self.id = k
        self.color = 'white'
        self.distance=sys.maxsize
        self.connectedTo = {}
        self.Pred = None
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

g = Graph()
g.addEdge('a','b',3)
g.addEdge('b','a',3)
g.addEdge('a','c',8)
g.addEdge('c','a',8)
g.addEdge('b','d',5)
g.addEdge('d','b',5)
g.addEdge('c','d',2)
g.addEdge('c','e',4)
g.addEdge('d','c',2)
g.addEdge('d','e',6)
g.addEdge('e','d',6)
g.addEdge('e','c',4)

g1 = Graph()
g1.addEdge('a','e',5)
g1.addEdge('e','a',5)
g1.addEdge('a','c',6)
g1.addEdge('c','a',6)
g1.addEdge('a','d',2)
g1.addEdge('d','a',2)
g1.addEdge('e','b',3)
g1.addEdge('b','e',3)
g1.addEdge('b','c',1)
g1.addEdge('c','b',1)
g1.addEdge('c','d',4)
g1.addEdge('d','c',4)
g1.addEdge('d','c',4)


def prim(start):
    vis = []
    s = [[0,start]]
    mincost = 0
    while len(s)>0:
        v = heapq.heappop(s)
        x = v[1]
        if(x in vis):
            continue
        mincost+=v[0]
        vis.append(x)
        for j in x.getConnections():
            if(j not in vis):
                heapq.heappush(s,[x.getWeight(j),j])
    return vis,mincost

ans1,cost1 = prim(g.getVertex('e'))
ans2,cost2 = prim(g1.getVertex('e'))
print(cost1)
print(cost2)
