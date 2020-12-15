import sys
from collections import deque as Queue
import inspect
from pythonds.graphs import Graph,Vertex

source_vertex = inspect.getsource(Graph)
print(source_vertex)

"""
class Node:
    def __init__(self,key):
        self.id = key
        self.connectedto = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.preDec = None
    
    def getVertex(self,n):
        if n not in 
    def setColor(self,color):
        self.color = color
    def setDistance(self,distance):
        self.distance = distance
    def setPred(self,pred):
        self.preDec = pred
    def getColor(self):
        return self.color
    def getDistance(self):
        return self.distance

    def addNeigh(self,nbr,weight=0):
        if nbr not in self.connectedto:
            self.connectedto[nbr] = weight
    def getNode(self,n):
        if n not in self.connectedto:
            return self.connectedto[n]
        return str("Whoa, This Node does not exist. What the hell are you playing at ?")
    def __contains__(self, item):
        return item in self.connectedto
    def connections(self):
        return self.connectedto.keys()
    def getweight(self,nbr):
        return self.connectedto[nbr]
    def getallweights(self):
        return self.connectedto.values()


class Graph:
    def __init__(self):
        self.numvertices=0
        self.graph = {}
    def addNode(self,key):
        if key not in self.graph:
            newNode = Node(key)
            self.graph[key] = newNode
        self.numvertices += 1
    def addEdge(self,fro,to,weight=0):
        if fro not in self.graph:
            newNode = Node(fro)
            self.graph[fro] = newNode
        if to not in self.graph:
            newNode = Node(to)
            self.graph[to] = newNode
        self.graph[fro].addNeigh(to,weight)
    def getNodes(self):
        return list(self.graph.keys())
    def __getitem__(self, item):
        return self.graph.fromkeys(item)

"""
def buildGraph():
    d = {}
    g = Graph()
    wfile = open("wordfile.txt",'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

g1 = buildGraph()


def bfs(g,start,counter=0):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.append(start)
    while vertQueue:
        currentvert = vertQueue.popleft()
        for nbr in currentvert.getConnections():
            if(nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentvert.getDistance() + 1)
                nbr.setPred(currentvert)
                vertQueue.append(nbr)
        currentvert.setColor('black')
    return g

ans = bfs(g1,g1.getVertex('FOOL'))

def traverse(y,counter=0):
    x = y
    while (x.getPred()):
        print(x.getId())
        counter+=1
        x = x.getPred()
    print(x.getId())
    return counter

answer = traverse(g1.getVertex('SAGE'))
print(answer)
