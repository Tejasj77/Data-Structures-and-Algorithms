import sys
class Vertex:
    def __init__(self,k):
        self.id = k
        self.color = 'white'
        self.distance=sys.maxsize
        self.connectedTo = {}
        self.Pred = None
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
        else:
            return None
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

class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0, 0)]
        self.currentSize = 0

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapArray = [(0, 0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 > self.currentSize:
            return -1
        else:
            if i * 2 + 1 > self.currentSize:
                return i * 2
            else:
                if self.heapArray[i * 2][0] < self.heapArray[i * 2 + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i // 2][0]:
                tmp = self.heapArray[i // 2]
                self.heapArray[i // 2] = self.heapArray[i]
                self.heapArray[i] = tmp
            i = i // 2

    def add(self, k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def decreaseKey(self, val, amt):
        # this is a little wierd, but we need to find the heap thing to decrease by
        # looking at its value
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt, self.heapArray[myKey][1])
            self.percUp(myKey)

    def __contains__(self, vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False
    def __iter__(self):
        return iter(self.heapArray)

def prim(g,start):
    pq = PriorityQueue()
    start.setDistance(0)
    mincost =0
    pq.buildHeap([(v.getDistance(),v) for v in g])
    visited = []
    while not pq.isEmpty():
        current = pq.delMin()
        if(current.getColor()!='white'):
            continue
        visited.append(current)
        current.setColor('gray')
        for nextvert in current.getConnections():
            if(nextvert.getColor()=='white'):
                pq.decreaseKey(nextvert,current.getWeight(nextvert))

        current.setColor('black')
    return visited
g = Graph()
g.addEdge('a','b',3)
g.addEdge('b','a',3)
g.addEdge('a','c',8)
g.addEdge('c','a',8)
g.addEdge('b','d',5)
g.addEdge('d','b',5)
g.addEdge('c','d',2)
g.addEdge('c','e',4)
g.addEdge('d','c',2)
g.addEdge('d','e',6)
g.addEdge('e','d',6)
g.addEdge('e','c',4)

g1 = Graph()
g1.addEdge('a','e',5)
g1.addEdge('e','a',5)
g1.addEdge('a','c',6)
g1.addEdge('c','a',6)
g1.addEdge('a','d',2)
g1.addEdge('d','a',2)
g1.addEdge('e','b',3)
g1.addEdge('b','e',3)
g1.addEdge('b','c',1)
g1.addEdge('c','b',1)
g1.addEdge('c','d',4)
g1.addEdge('d','c',4)
g1.addEdge('d','c',4)

#ans = prim(g,g.getVertex('a'))
ans = prim(g1,g1.getVertex('a'))
i = len(ans)-1
sum=0
while(i!=0):
    sum=sum+(ans[i].getWeight(ans[i-1]))
    i=i-1
print(sum)