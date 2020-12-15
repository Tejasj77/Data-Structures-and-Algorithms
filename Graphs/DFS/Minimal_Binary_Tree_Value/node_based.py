orphans = []
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
    def getValue(self):
        return self.value
    def setValue(self,val):
        self.value +=val
    def getConnections(self):
        return self.connectedTo.keys()
    def __str__(self):
        return "ID:" + str(self.id) + " Value: " + str(self.value) + " Color:" + str(self.color) + "ConnectedTo\n" + \
               f"{[(i.id) for i in self.connectedTo ]}"

class Graph:
    def __init__(self):
        self.graph = {}
        self.time = 0
    def addVertex(self,n,v):
        nv = Vertex(n,v)
        self.graph[n] = nv
        return nv
    def addEdge(self,f,t,cost=0):
        self.graph[f].addNeigh(self.graph[t],cost)
    def getVertex(self,n):
        return self.graph[n]
    def __iter__(self):
        return iter(self.graph.values())

def dfs(g1,start,path):
    if(start.getColor()=='white'):
        path.append(start)
        start.setColor('gray')
        if len(list(start.getConnections()))%2!=0:
            orphans.append(start)
        for nextnode in start.getConnections():
            if(nextnode.getColor()=='white'):
                temp = dfs(g1,nextnode,path)
                start.setValue(nextnode.getValue())
        start.setColor('black')
    return g1

def bfs(g,start,summer=0):
    summer = start.getValue()
    queue = []
    queue.append(start)
    while queue:
        current = queue.pop()
        for nbr in current.getConnections():
            summer += nbr.getValue()
            queue.append(nbr)
    return summer

#g = Graph()
first_inp = list(map(int,input().split()))
n,val = first_inp[0],first_inp[1]
#print(n)
node_values = input().split()
edge_list = []
for j in range(n-1):
    edge_list.append(list(map(int,input().split())))

#print(edge_list)
"""
i = 0
for j in range(1,len(node_values)+1):
    g.addVertex(j,int(node_values[j-1]))

for it in edge_list:
    g.addEdge(it[i],it[i+1])

ans = dfs(g,g.getVertex(1),[])
print(f"{[i.id for i in ans]}")
answer = bfs(g,g.getVertex(1))
print(answer)
print(f"{[i.id for i in orphans]}")
"""
g = Graph()
i = 0
for j in range(1, len(node_values) + 1):
    g.addVertex(j, int(node_values[j - 1]))
for it in edge_list:
    g.addEdge(it[i], it[i + 1])
new_node = g.addVertex(len(node_values)+1, val)
final_g = dfs(g,g.getVertex(1),[])

for i in final_g:
    print(i)

for iterator in range(len(orphans)):
    final_g.addEdge(new_node.id,orphans[iterator].id)
    sum1 = bfs(final_g,final_g.getVertex(1))
    print(sum1)