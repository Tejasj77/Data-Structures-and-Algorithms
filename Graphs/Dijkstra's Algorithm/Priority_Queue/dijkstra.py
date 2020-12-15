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
        return "The ID: " + str(self.id) + " Color: " + str(self.color) + " Distance:" + str(self.distance)\
    + "Connections: " + f"{[i.id for i in self.connectedTo]}" + str(self.getPred())

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

g = Graph()
g.addEdge('u','v',2)
g.addEdge('u','x',1)
g.addEdge('u','w',5)
g.addEdge('v','w',3)
g.addEdge('v','x',2)
g.addEdge('v','u',2)
g.addEdge('w','z',5)
g.addEdge('w','y',1)
g.addEdge('w','v',3)
g.addEdge('w','x',3)
g.addEdge('x','y',1)
g.addEdge('x','u',1)
g.addEdge('x','w',3)
g.addEdge('x','v',2)
g.addEdge('y','z',1)
g.addEdge('y','x',1)
g.addEdge('y','w',1)
g.addEdge('z','w',5)
g.addEdge('z','y',1)

def dijkstra(g,start):
    pq = PriorityQueue()
    start.setDistance(0)
    # Nodes and the default values are set in the Priority Heap
    pq.buildHeap([(v.getDistance(),v) for v in g])
    while not pq.isEmpty():
        # Node with the least distance is popped(delMin arranges the queue also)
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            # The current distance + the distance between the current node
            # and the next node
            newdist = currentVert.getDistance()\
            + currentVert.getWeight(nextVert)
            #If the above distance is less than the default distance
            if newdist < nextVert.getDistance():
                nextVert.setDistance(newdist)
                nextVert.setPred(currentVert)
                #Rearrange the node inside the binary heap as the distance has now changed.
                pq.decreaseKey(nextVert,newdist)

dijkstra(g,g.getVertex('z'))





