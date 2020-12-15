from collections import deque as Queue
import sys

class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(
            self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

    def getId(self):
        return self.id


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    start.setColor('gray')
    verQ = Queue()
    verQ.append(start)
    while verQ:
        currentvert = verQ.popleft()

        for neigh in currentvert.getConnections():
            if(neigh.getColor() == 'white'):
                neigh.setColor('gray')
                neigh.setDistance(currentvert.getDistance() + 1)
                verQ.append(neigh)
                neigh.setPred(currentvert)
        currentvert.setColor('black')
    return g

def bfs1(g,start):
    counter = 0
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.append(start)
    while vertQueue:
        currentvert = vertQueue.popleft()
        for nbr in currentvert.getConnections():
            if(nbr.getColor() == 'white'):
                nbr.setColor('gray')
                counter = currentvert.getDistance() + 1
                nbr.setDistance(currentvert.getDistance() + 1)
                nbr.setPred(currentvert)
                vertQueue.append(nbr)
                print(vertQueue)
        currentvert.setColor('black')

    return g
#num_nodes = int(input())
g = Graph()
"""
for i in range(num_nodes - 1):
    inp_list = None
    inp_list = input().split()
    g.addEdge(int(inp_list[0]), int(inp_list[1]))

ans = bfs(g, g.getVertex(1))
x = int(input())
counter = 1
for i in ans:
    if(i.getDistance()==x):
        counter+=1
print(counter)"""

file = open("node_file.txt",'r')
for i in file:
    list1 = None
    list1 = i.split()
    g.addEdge(int(list1[0]),int(list1[1]))
    print(list1)

ans = bfs1(g,g.getVertex(5))
x =4
