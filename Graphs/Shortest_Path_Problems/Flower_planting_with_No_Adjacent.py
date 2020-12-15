class Vertex:
    def __init__(self,key):
        self.id = key
        self.dist = 0
        self.connectedTo = {}
        self.color = 'white'

    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def getDistance(self):
        return self.dist
    def setDistance(self,distance):
        self.dist = distance
    def getConnections(self):
        return self.connectedTo.keys()
    def __str__(self):
        return "ID:" + str(self.id) + " Distance: " + str(self.dist) +  " Color:" + str(self.color) + "ConnectedTo\n" + \
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
g.addEdge(1,2)
g.addEdge(2,1)
# g.addEdge(1,3)
# g.addEdge(3,1)
g.addEdge(1,4)
g.addEdge(4,1)
g.addEdge(2,4)
g.addEdge(4,2)
g.addEdge(3,4)
g.addEdge(4,3)
g.addEdge(2,3)
g.addEdge(3,2)

g1 = Graph()
g1.addEdge(1,2)
g1.addEdge(2,1)
g1.addEdge(3,4)
g1.addEdge(4,3)

g2 = Graph()
for i in range(1,1001):
    g2.addVertex(i)
g2.addEdge(1,2)
g2.addEdge(2,1)

def travel(graph):
    choices = [1,2,3,4]
    for node in graph:
        if(node.getDistance()==0):
            choice_iter = 0
            flag=False
            temp = []
            for nbr in node.getConnections():
                if(nbr.getDistance()!=0):
                    flag=True
                    temp.append(nbr.getDistance())
            if(flag):
                for i in choices:
                    if i not in temp:
                        node.setDistance(i)
            else:
                node.setDistance(choices[choice_iter])
                for nbr in node.getConnections():
                    choice_iter+=1
                    nbr.setDistance(choices[choice_iter])

travel(g2)
distances = [0]*len(g2)
for i in g2:
    j = i.id-1
    distances[j] = i.getDistance()
print(distances)