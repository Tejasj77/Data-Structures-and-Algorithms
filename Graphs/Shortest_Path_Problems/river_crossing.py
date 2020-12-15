import sys
class Vertex:
    def __init__(self,k):
        self.id = k
        self.color = 'white'
        self.distance=sys.maxsize
        self.connectedTo = {}
        self.Pred = None
        self.next = None
    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def setDistance(self,dist):
        self.distance = dist
    def getDistance(self):
        return self.distance
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
        return "ID:" + str(self.id) + "Value: " + str(self.distance) + " Color:" + str(self.color) + "ConnectedTo\n" + \
               f"{[(i.id) for i in self.connectedTo]}"


class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self,key):
        if key not in self.graph:
            nv = Vertex(key)
            self.graph[key] = nv
            return nv
    def addEdge(self,f,t,cost=0):
        if f not in self.graph:
            nv1 = Vertex(f)
            self.graph[f] = nv1
        if t not in self.graph:
            nv2 = Vertex(t)
            self.graph[t] = nv2
        self.graph[f].addNeigh(self.graph[t],cost)
    def getVertex(self,key):
        return self.graph[key]
    def __iter__(self):
        return iter(self.graph.values())
    def __len__(self):
        return len(self.graph)

g = Graph()
t = int(input())
for iterator in range(t):

    num_rocks = int(input())
    coor = []
    for i in range(num_rocks):
        coor.append(list(map(int,input().split())))
        #g.addVertex((xco,yco)).setDistance(r1)
    final_point,start_point = list(map(int,input().split()))
    print(final_point,start_point)
    g.addVertex(final_point).setDistance(0)
    g.addVertex(start_point).setDistance(0)
    #coor.append([0,start_node,0])
    #coor.append([0,final_node,0])
    #g.addVertex((0,start_node)).setDistance(0)
    #g.addVertex((0,final_node)).setDistance(0)
    for i in coor:
        temp = g.addVertex((i[0],i[1]))
        temp.setDistance(i[2])

    print(coor)

    for i in coor:
        for j in coor:
            if j!=i:
                x = ((i[0]-j[0])*(i[0]-j[0]))
                y = ((i[1]-j[1])*(i[1]-j[1]))
                r1 = i[2]
                r2 = j[2]
                if((x+y)<((r1+r2)*(r1+r2))):
                    g.addEdge((i[0],i[1]),(j[0],j[1]))
    for i in coor:
        if(start_point<=i[1]<=final_point and (i[1]+i[2])<=final_point):
            g.addEdge((i[0],i[1]),final_point)

for i in g:
    print(i)