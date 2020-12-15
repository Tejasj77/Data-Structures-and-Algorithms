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
    def __len__(self):
        return len(self.graph)

g = Graph()
g.addEdge('a','b',6)
g.addEdge('a','e',7)
g.addEdge('b','d',-3)
g.addEdge('b','c',5)
g.addEdge('b','e',8)
g.addEdge('c','b',-2)
g.addEdge('d','c',7)
g.addEdge('d','a',2)
g.addEdge('e','b',-3)
print(len(g))

def bellman_ford(g,start):
    start.setDistance(0)
    i=0
    while i<len(g)-1:
        for node in g:
            for nbr in node.getConnections():
                if(nbr.getDistance()>(node.getDistance()+node.getWeight(nbr))):
                    nbr.setDistance(node.getDistance()+node.getWeight(nbr))
                    nbr.setPred(node)
        i+=1
    for node in g:
        for nbr in node.getConnections():
            if(nbr.getDistance()>(node.getDistance()+node.getWeight(nbr))):
                return False
    return True

print(bellman_ford(g,g.getVertex('a')))
