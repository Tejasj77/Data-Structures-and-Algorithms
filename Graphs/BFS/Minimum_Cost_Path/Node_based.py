import sys
from collections import defaultdict
class Node:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = sys.maxsize
    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def setDistance(self,dist):
        self.distance = dist
    def getDistance(self):
        return self.distance
    def getconnections(self):
        return self.connectedTo.keys()
    def getWeight(self,n):
        return self.connectedTo[n]
    def getonlynodes(self):
        return list(self.connectedTo.keys())

    def __iter__(self):
        return iter(self.connectedTo.items())
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":dist " + str(self.distance) + ":pred \n\t[" + f"{[i for i in self.connectedTo]}"+ "]\n"

class Graph:
    def __init__(self):
        self.graph = {}
    def addNode(self,n):
        newnode = Node(n)
        self.graph[n] = newnode
        return newnode
    def addEdge(self,f,t,cost):
        if f not in self.graph:
            nv1 = self.addNode(f)
        if t not in self.graph:
            nv2 = self.addNode(t)
        self.graph[f].addNeigh(self.graph[t],cost)
    def getNode(self,n):
        if n in self.graph:
            return self.graph[n]
        else:
            return None
    def __iter__(self):
        return iter(self.graph.values())

def bfs(g,start,vertarr,end):
    weighter = []
    start.setDistance(0)
    start.setColor('gray')
    queue = []
    queue.append(start)
    traverse = True
    #done = False
    while queue:
        """
        current = queue.pop()
        if(current.id==end.id):
            break
        for vert in vertarr:
            for ids in current.getonlynodes():
                if vert==ids.id:
                    #print(vert)
                    nbr = g.getNode(vert)
                    if(nbr.getColor()=='white' and nbr!=current):
                        nbr.setColor('gray')
                        dist = current.getWeight(nbr)
                        nbr.setDistance(dist)
                        #print(current.getWeight(nbr))
                        queue.append(nbr)
                        traverse = False
        if(traverse==True):
            for nbr in current.getconnections():
                if(nbr.getColor()=='white'):
                    nbr.setColor('gray')
                    dist = current.getWeight(nbr)
                    nbr.setDistance(dist)
                    queue.append(nbr)
        
            min = sys.maxsize
            min_node = current
            print(min_node.id)
            for nbr in current.getconnections():
                if(nbr.getColor()=='white'):
                    if current.getWeight(nbr)>0 and current.getWeight(nbr)<min:
                        min = current.getWeight(nbr)
                        min_node = nbr

            min_node.setColor('gray')
            queue.append(min_node)
            if(min_node.id == end.id):
                min_node.setColor('black')
                done = True

        current.setColor('black')
    #print(weighter)
    """
        current = queue.pop()
        for nbr in current.getconnections():
            if(nbr.getColor()=='white'):
                nbr.setColor('gray')
                prev_dist = current.getDistance()
                dist = current.getWeight(nbr)
                nbr.setDistance(dist+prev_dist)
                queue.append(nbr)
        current.setColor('black')
    return g

g = Graph()
g.addEdge(0,1,2)
g.addEdge(0,7,3)
g.addEdge(0,3,2)
g.addEdge(3,0,1)
g.addEdge(3,5,7)
g.addEdge(5,6,2)
g.addEdge(7,5,6)
g.addEdge(7,4,5)
g.addEdge(1,4,4)
g.addEdge(4,6,4)

vertices = []
first = g.getNode(0)
third = g.getNode(3)


ans = bfs(g,g.getNode(0),vertices,g.getNode(6))
for i in ans:
    print(i)


