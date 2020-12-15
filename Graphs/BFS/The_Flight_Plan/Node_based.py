class Airport:
    def __init__(self,id):
        self.id = id
        self.status = 'running'
        self.time =0
        self.connectedTo = {}
        self.color = 'white'

    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def setTime(self,t):
        self.time = t
    def getTime(self):
        return self.time
    def setStatus(self,stat):
        self.status = stat
    def getStatus(self):
        return self.status
    def getConnections(self):
        return self.connectedTo.keys()
    def __str__(self):
        return "ID of airport" + "\t" + str(self.id) + "\t" + str(self.status) + "\t" + str(self.time) + \
               "\t" +str(self.connectedTo.keys())

class Graph:
    def __init__(self):
        self.graph = {}
    def addAirport(self,air):
        newap = Airport(air)
        self.graph[air] = newap
        return newap
    def addRoute(self,f,t,cost=0):
        if f not in self.graph:
            newap = self.addAirport(f)
        if t not in self.graph:
            newapt = self.addAirport(t)
        self.graph[f].addNeigh(self.graph[t],cost)
    def getAirport(self,key):
        if key in self.graph:
            return self.graph[key]
        else:
            return None
    def __iter__(self):
        return iter(self.graph.values())

def bfs(g,start,tt,gap,end):
    start.setDistance(0)
    start.setColor('gray')
    queue = []
    queue.append(start)
    while queue and start.id != end.id:
        currentap = queue.pop()
        for nbr in currentap.getConnections():
            if(nbr.getColor()=='white' and nbr.getDistance()%gap !=0):
                nbr.setColor('gray')
                nbr.setDistance(currentap.getDistance()+tt)
                queue.append(nbr)
        currentap.setColor('black')
    return g


g = Graph()
first_input = input().split()
for _ in range(int(first_input[1])):
    conn = input().split()
    g.addRoute(int(conn[0]),int(conn[1]))
    g.addRoute(int(conn[0]), int(conn[1]))
second_input = input().split()
for i in g:
    print(i)
print(second_input)
