import sys

class Vertex:
    def __init__(self,k,v):
        self.id = k
        self.value = v
        self.color = 'white'
        self.distance=[sys.maxsize,sys.maxsize]
        self.connectedTo = {}
        self.Pred = None
        self.next = None
    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def setfrontDistance(self,dist):
        self.distance[0] = dist
    def setbackDistance(self,dist):
        self.distance[1]=dist
    def getDistance(self):
        return self.distance
    def getfrontDistance(self):
        return self.distance[0]
    def getbackDistance(self):
        return self.distance[1]
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
        return "ID:" + str(self.id) + "Value: " + str(self.value) + ' Distance: ' + str(self.distance) + " Color:" + str(self.color) + "ConnectedTo\n" + \
               f"{[(i.id) for i in self.connectedTo]}"


class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self,key,value):
        if key not in self.graph:
            nv = Vertex(key,value)
            self.graph[key] = nv
            return nv
    def addEdge(self,f,v1,t,v2,cost=0):
        if f not in self.graph:
            nv1 = Vertex(f,v1)
            self.graph[f] = nv1
        if t not in self.graph:
            nv2 = Vertex(t,v2)
            self.graph[t] = nv2
        self.graph[f].addNeigh(self.graph[t],cost)
    def getVertex(self,value):
        for k,v in self.graph.items():
            if value==v.value:
                return self.graph[k]

    def __iter__(self):
        return iter(self.graph.values())
    def __len__(self):
        return len(self.graph)

g = Graph()
S = input()
C = input()
for i in range(len(S)-1):
    if S[i+1]:
        g.addEdge(i,S[i],i+1,S[i+1])
        g.addEdge(i+1,S[i+1],i,S[i])

def dfs(graph,inp):
    path = []
    traverse = []
    for node in graph:
        traverse.append(node)
        if(node.value==inp):
            node.setColor('black')
            node.setfrontDistance(0)
            node.setbackDistance(0)
            continue
        else:
            flag=False
            for nbr in node.getConnections():
                if(nbr.value==inp):
                    flag=True
                    node.setfrontDistance(1)
                    node.setbackDistance(0)
                    node.setColor('gray')
                    i = 1
                    while len(path) != 0:
                        current = path.pop()
                        i += 1
                        current.setfrontDistance(i)
                        current.setColor('gray')

            if flag!=True:
                #node.setDistance(0)
                path.append(node)

    path = []
    new_traverse = traverse[::-1]
    for i in new_traverse:
        if (i.value == inp):
            i.setbackDistance(0)
            continue
        else:
            backflag=False
            for node in i.getConnections():
                if(node.value==inp):
                    backflag=True
                    i.setbackDistance(1)
                    node.setColor('gray')
                    j = 1
                    while len(path) != 0:
                        current = path.pop()
                        j += 1
                        current.setbackDistance(j)
                        current.setColor('gray')

            if backflag != True:
                # node.setDistance(0)
                path.append(i)



dfs(g,C)
shortest = [0]*len(g)
for i in g:
    iter=sys.maxsize
    for j in i.getDistance():
        if j<iter:
            iter=j
    shortest[i.id] = iter

print(shortest)