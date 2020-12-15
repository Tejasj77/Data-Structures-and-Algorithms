class Node:
    def __init__(self,key):
        self.id = key
        self.connectedto ={}
    def addNeigh(self,nbr,weight=0):
        if nbr not in self.connectedto:
            self.connectedto[nbr] = weight
    def getNode(self,n):
        if n in self.connectedto:
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
        return self.graph.keys()
    def __getitem__(self, item):
        return self.graph[item]


g = Graph()

g.addNode(0)
g.addNode(1)
g.addNode(2)
g.addEdge(0,1,5)
g.addEdge(1,2)
