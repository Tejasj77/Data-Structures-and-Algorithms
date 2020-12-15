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
        self.time = 0
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

def dfs1(g1,start,end,path):
    if end.id==start.id:
        return path
    if(start.getColor()=='white'):
        path.append(start)
        start.setColor('gray')
        for nextnode in start.getConnections():
            if(nextnode.getColor()=='white'):
                temp = dfs1(g1,nextnode,end,path)
        start.setColor('black')
    return path


g = Graph()
g.addEdge('1','1.2')
g.addEdge('1','1.3')
g.addEdge('1','1.4')
g.addEdge('1.2','1.2.1')
g.addEdge('1.2','1.2.2')
g.addEdge('1.2.1','1.2.1.1')
g.addEdge('1.3','1.3.1')
g.addEdge('1.4','1.4.1')
g.addEdge('1.4.1','1.4.1.1')
g.addEdge('1.4.1.1','1.4.1.1.1')
g.addEdge('1.4.1.1','1.4.1.1.2')

print(g.getVertex('1'))
print(g.getVertex('1.4'))
#fin1,fin2 = dfs(0,[],g.getVertex('1'),6)
ans = dfs1(g,g.getVertex('1'),g.getVertex('1.4'),[])
# for i in g:
#     print(i)
print(f"{[i.id for i in ans]}")