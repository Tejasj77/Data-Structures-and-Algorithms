from collections import defaultdict
import sys

class Vertex:
    def __init__(self,key):
        self.id = key
        self.dist = sys.maxsize
        self.connectedTo = defaultdict(list)
        self.color = 'white'

    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr].append(weight)
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def getDistance(self):
        return self.dist
    def setDistance(self,distance):
        self.dist = distance
    def getWeight(self,node):
        return self.connectedTo[node]
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
n = 3
for i in range(n):
    g.addVertex(i)
red_list = [[0,1],[0,2]]
blue_list = [[1,0]]
for i in red_list:
    g.addEdge(i[0],i[1],0)
for j in blue_list:
    g.addEdge(j[0],j[1],1)

def bfs(graph,start):
    start.setDistance(0)
    start.setColor('gray')
    queue = []
    level = 0
    edge_wt = 2
    queue.append(start)
    done = False
    visited =[0]*(len(graph))
    visit=0
    while queue and not done:
        print(queue)
        print(visit)
        current=queue.pop()
        print(current.id)
        for nbr in current.getConnections():
            print(nbr.id)
            for wt in current.getWeight(nbr):
                if(wt!=edge_wt):
                    if(nbr.getColor()=='white'):
                        edge_wt=wt
                        level+=1
                        nbr.setDistance(level)
                        visited[nbr.id]=level
                        visit+=1
                        nbr.setColor('gray')
                        queue.append(nbr)
                        break
                    else:
                        if(visit == len(graph)):
                            done = True
                            queue=None
                            return visited
                        else:
                            edge_wt = wt
                            level+=1
                            queue.append(nbr)
                        break
            current.setColor('black')
    return visited



ans=bfs(g,g.getVertex(0))
for i in g:
    print(i)
print(ans)