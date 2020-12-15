class Node:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.time = 0
    def addNeigh(self,nbr,weight=0):
        if nbr not in self.connectedTo:
            self.connectedTo[nbr] = weight
    def getNode(self,n):
        if n in self.connectedTo:
            return self.connectedTo[n]
        return "Whoa, This node does not exist. What are you playing at ?"
    def getColor(self):
        return self.color
    def setColor(self,colour):
        self.color = colour
    def settime(self,time):
        self.time = time
    def __contains__(self, item):
        return item in self.connectedTo
    def getConnections(self):
        return self.connectedTo.keys()
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    def getallweights(self):
        return self.connectedTo.values()
    def __str__(self):
        return str(self.id) + f"{[i.id for i in self.connectedTo]}" + " Inform Time is " + str(self.time)

class Graph:
    def __init__(self):
        self.graph = {}
        self.level = 0
    def addNode(self,k):
        if k not in self.graph:
            newNode = Node(k)
            self.graph[k] = newNode
            return newNode
    def addEdge(self,fro,to,weight=0):
        if fro not in self.graph:
            newnode1 = self.addNode(fro)
        if to not in self.graph:
            newnode2= self.addNode(to)
        self.graph[fro].addNeigh(self.graph[to],weight)
    def getNode(self,n):
        return self.graph[n]
    def __iter__(self):
        return iter(self.graph.values())
    def __len__(self):
        return len(self.graph)

def bfs(graph,start):
    time_set = [0]*len(graph)
    start.setColor('gray')
    queue = []
    queue.append(start)

    while queue:
        neigh = ()
        current = queue.pop()
        time_set[current.id] = current.time
        iter=0
        for nbr in current.getConnections():
            if(nbr.getColor()=='white'):
                nbr.setColor('gray')
                #print(time_set)
                queue.append(nbr)
                break
        current.setColor('black')
    return time_set

def dfs(graph,start,time_set):
    if(start.getColor()=='white'):
        start.setColor('gray')
        for nbr in start.getConnections():
            if(nbr.getColor()=='white'):



#manager = [2,2,-1,2,2,2]
#informTime = [0,0,1,0,0,0]

#manager = [1,2,3,4,5,6,-1]
#informTime = [0,6,5,4,3,2,1]

#manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
#informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

#manager = [-1,5,0,6,7,0,0,0]
#informTime = [89,0,0,0,0,523,241,519]

#manager = [2,2,-1,2,2,2]
#informTime = [0,0,1,0,0,0]

#manager = [3,3,-1,2]
#informTime = [0,0,162,914]

#manager = [2,2,-1,2,2,2]
#informTime = [0,0,1,0,0,0]

manager = [-1,5,0,6,7,0,0,0]
informTime = [89,0,0,0,0,523,241,519]
g = Graph()
iteration=0
extra_addition=0
for i,j in zip(manager,informTime):
    g.addEdge(i,iteration,j)
    node = g.getNode(iteration)
    node.settime(j)
    iteration+=1

for i in g:
    print(i)
initiation = g.getNode(-1)
next = None
for i in initiation.getConnections():
    next = i
print(next.id)
ans = bfs(g,next)
print(ans)
sum = 0
for i in ans:
    sum+=i
print(sum)

