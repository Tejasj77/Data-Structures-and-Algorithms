class Vertex:
    def __init__(self,id):
        self.id = id
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.preced = None
    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def setPreced(self,n):
        self.preced = n
    def setColor(self,color):
        self.color = color
    def setDistance(self,dist):
        self.distance = dist
    def getDistance(self):
        return self.distance
    def getColor(self):
        return self.color
    def getPreced(self):
        return self.preced
    def getconnections(self):
        return self.connectedTo.keys()

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":dist " + str(self.distance) + ":pred \n\t[" + str(self.preced) + "]\n"


class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self,key):
        if key not in self.graph:
            vert = Vertex(key)
            self.graph[key] = vert
            return vert
    def addEdge(self,f,t,cost=0):
        if f not in self.graph:
            nv1 = self.addVertex(f)
        if t not in self.graph:
            nv2 = self.addVertex(t)
        self.graph[f].addNeigh(self.graph[t],cost)
    def getVertex(self,key):
        return self.graph[key]
    def __iter__(self):
        return iter(self.graph.values())

def bfs(g,start):
    start.setDistance(0)
    start.setColor('gray')
    queue = []
    queue.append(start)
    while queue:
        currentvert = queue.pop()
        for nbr in currentvert.getconnections():
            if(nbr.getColor()=='white'):
                nbr.setColor('gray')
                nbr.setDistance(currentvert.getDistance()+1)
                queue.append(nbr)
        currentvert.setColor('black')
    return g

file = open("input.txt","r")
counter,flag = 0,False
g = Graph()
for i in file:
    if(flag==False):
        list1 = i.split()
        num_edges = int(list1[1])
        flag=True
    else:
        counter +=1
        if(counter<num_edges+1):
            list2 = i.split()
            g.addEdge(int(list2[0]),int(list2[1]))
            g.addEdge(int(list2[1]), int(list2[0]))


x = int(input())
fin_list = []
for i in range(x):
    list1 = input().split()
    ans = bfs(g,g.getVertex(int(list1[0])))
    for i in ans:
        if(i.getDistance()==int(list1[1])):
            fin_list.append(i.id)
    print(len(fin_list))







