class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def getConnections(self):
        return self.connectedTo.keys()
    def __str__(self):
        return "ID:" + str(self.id) +  " Color:" + str(self.color) + "ConnectedTo\n" + \
               f"{[(i.id) for i in self.connectedTo ]}"

class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self,n):
        if n not in self.graph:
            nv = Vertex(n)
            self.graph[n] = nv
            return nv
    def addEdge(self,f,t,cost=0):
        if f not in self.graph:
            nv1 = self.addVertex(f)
        if t not in self.graph:
            nv2 = self.addVertex(t)
        self.graph[f].addNeigh(self.graph[t],cost)
    def getVertex(self,n):
        return self.graph[n]
    def __iter__(self):
        return iter(self.graph.values())
    def __len__(self):
        return len(self.graph)

g = Graph()
g.addEdge(0,1),g.addEdge(0,2),g.addEdge(2,5),g.addEdge(3,4),g.addEdge(4,2)
"""
g.addEdge(0,1)
g.addEdge(1,4)
g.addEdge(3,1)
g.addEdge(2,1)
g.addEdge(2,4)
g.addEdge(3,0)

g.addEdge(0,1)
g.addEdge(3,2)
g.addEdge(4,1)
g.addEdge(2,1)
g.addEdge(4,2)
g.addEdge(3,4)
g.addEdge(0,2)
g.addEdge(4,0)
"""

#81.8MB and 1728ms
def travel(graph,n):
    list1 = []
    for node in graph:
        if(node.getColor()=='white'):
            node.setColor('gray')
            list1.append(node)
            n-=1
        for nbr in node.getConnections():
            if(nbr.getColor()=='white'):
                nbr.setColor('gray')
                n-=1
            elif(nbr.getColor()=='gray'):
                if nbr in list1:
                    list1.remove(nbr)
    return list1

#82.8 MB and 1608ms
def travel2(graph):
    ng_set = set()
    fin_set = []
    for node in graph:
        for nbr in node.getConnections():
            ng_set.add(nbr)
    for node in graph:
        if node not in ng_set:
            fin_set.append(node.id)
    return fin_set
ans1 = travel2(g)
ans2 = travel(g,len(g))
print(f"{[i for i in ans1]}")
print(f"{[i.id for i in ans2]}")
