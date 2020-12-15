class Vertex:
    def __init__(self,key,value):
        self.id = key
        self.value = value
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
        return "ID:" + str(self.id) + "Value: " + str(self.value) +  " Color:" + str(self.color) + "ConnectedTo\n" + \
               f"{[(i.id,i.value) for i in self.connectedTo ]}"

class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self,n,val):
        if n not in self.graph:
            nv = Vertex(n,val)
            self.graph[n] = nv
            return nv
    def addEdge(self,f,n1,t,n2,cost=0):
        if f not in self.graph:
            nv1 = self.addVertex(f,n1)
        if t not in self.graph:
            nv2 = self.addVertex(t,n2)
        self.graph[f].addNeigh(self.graph[t],cost)
    def getVertex(self,n):
        return self.graph[n]
    def __iter__(self):
        return iter(self.graph.values())

g1 = Graph()
counter=0
g = [[1,1,0,1,0],
     [0,1,0,0,0],
     [1,0,0,1,1],
     [0,0,0,0,0],
     [1,0,1,0,1]]

def pos_legal(x):
    if x>-1 and x<5:
        return True

def convertNode(a,b):
    return (a,b)

def graph_creator(a,b):
    mov_offsets = [(-1,-1),(-1,0),(-1,1),
                   (0,-1),(0,1),
                   (1,-1),(1,0),(1,1)]
    #print(f"The node {g[a][b]} has neighbours at ")
    nodeID = g1.addVertex(convertNode(a,b),g[a][b])
    for loc in mov_offsets:
        newX = a+loc[0]
        newY = b+loc[1]
        if pos_legal(newX) and pos_legal(newY) and g[newX][newY]==1:
            #print(f"{newX,newY} and it is {g[newX][newY]}")
            newID = convertNode(newX,newY)
            g1.addEdge(convertNode(a,b),g[a][b],newID,g[newX][newY])


for i in range(len(g)):
    for j in range(len(g[i])):
        #Iterate through the 8 neighbouring vertices
        if(g[i][j]==1):
            graph_creator(i,j)

def dfs(g1,start):
    if(start.getColor()=='white'):
        start.setColor('gray')
        for nextnode in start.getConnections():
            if(nextnode.getColor()=='white'):
                dfs(g1,nextnode)
        start.setColor('black')
        return True
    return False



start_vertex = g1.getVertex((0,0))
#answer = dfs(g1,start_vertex)
for i in range(len(g)):
    for j in range(len(g[i])):
        #Iterate through the 8 neighbouring vertices
        if(g[i][j]==1):

            if(dfs(g1,g1.getVertex((i,j)))):
                counter+=1

print(counter)