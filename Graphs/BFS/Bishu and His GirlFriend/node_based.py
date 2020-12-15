import sys
from collections import OrderedDict
class Vertex:
    def __init__(self,id):
        self.id=id
        self.connectedTo = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.girl_present = False
#        self.position = [None]

    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getDistance(self):
        return self.distance
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def setDistance(self,dist):
        self.distance = dist
    def getconnections(self):
        return self.connectedTo.keys()
    def setGirl(self,bool):
        self.girl_present=bool
    def sort_now(self):
        return OrderedDict(sorted(self.connectedTo.keys()))
    def __iter__(self):
        return iter(self.connectedTo.items())
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":dist " + str(self.distance) + "Girl"+str(self.girl_present)+\
               ":pred \n\t[" + \
               f"{[(i.id,i.color,i.girl_present) for i in self.connectedTo]}" + "]\n"

class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self,key):
        nv = Vertex(key)
        self.graph[key] = nv
        return nv
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

def bfs(start,lookout_list):
    start.setDistance(0)
    start.setColor('gray')
    queue = []
    queue.append(start)
    while queue:
        current = queue.pop()
        for nbr in current.getconnections():
            if(nbr.getColor()=='white'):
                if(int(nbr.id) in lookout_list):
                    nbr.setGirl(True)
                nbr.setColor('gray')
                nbr.setDistance(current.getDistance()+1)
                queue.append (nbr)
        current.setColor('black')
    return g


g = Graph()
node_number = int(input())
edge_list = []
for i in range(node_number-1):
    edge_list.append(input().split())
for i in edge_list:
    looper =0
    #print(i[looper],i[looper+1])
    g.addEdge(int(i[looper]),int(i[looper+1]))
    g.addEdge(int(i[looper+1]), int(i[looper]))

number_girls = int(input())
girls_nodes = []
for i in range(number_girls):
    girls_nodes.append(int(input()))

ans = bfs(g.getVertex(1),girls_nodes)
min_node = None
min = sys.maxsize

for i in ans:
    if(i.girl_present==True):
        if(i.distance<min and i.distance!=0):
            min = i.distance
            min_node = i
print(min_node.id)