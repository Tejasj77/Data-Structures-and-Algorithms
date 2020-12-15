
class City:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.status = 'operate'
    def addNeigh(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def getconnections(self):
        return self.connectedTo.keys()
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
    def setStatus(self,stat):
        self.status = stat
    def getStatus(self):
        return self.status

    def __str__(self):
        return "ID of airport" + "\t" + str(self.id) + "\t" + str(self.status) + "\t" + \
               "\t" + str(self.connectedTo.keys())


class Graph:
    def __init__(self):
        self.graph = {}
    def addCity(self,city):
        nv = City(city)
        self.graph[city] = nv
        return nv

    def addEdge(self,f,t,cost=0):
        if f not in self.graph:
            nv1 = self.addCity(f)
        if t not in self.graph:
            nv2 = self.addCity(t)
        self.graph[f].addNeigh(self.graph[t],cost)
    def getCity(self,key):
        if key in self.graph:
            return self.graph[key]
        else:
            return None

    def __iter__(self):
        return iter(self.graph.values())

def bfs(g,start):
    counter = 0
    queue = []
    queue.append(start)
    while queue:
        current = queue.pop()
        if(current.getStatus()=='operate'):
            start.setColor('gray')
            for nbr in current.getconnections():
                if(nbr.getColor()=='white'):
                    nbr.setColor('gray')
                    queue.append(nbr)
            current.setColor('black')
    return g

def graph_creation(edges,blocks):
    g = Graph()
    j =0
    for j in range(len(edges)):
        g.addEdge(edges[j][0],edges[j][1])
        g.addEdge(edges[j][1], edges[j][0])
        j+=1
    counter = 0
    for i in g:
        if (blocks[counter] == 1):
            i.setStatus('block')
        counter += 1
    return g

def main():
    graph_list = []
    first_input = int(input())
    edge_list = []
    node_list = []
    for iter in range(first_input-1):
        a = input().split()
        b = [int(i) for i in a]
        edge_list.append(b)
        for i in a:
            if int(i) not in node_list:
                node_list.append(int(i))

    block_list = list(map(int, input().split()))
    ans = graph_creation(edge_list,block_list)
    for iter in range(first_input):
        ans = graph_creation(edge_list, block_list)
        graph_list.append(bfs(ans,ans.getCity(node_list[iter])))
    counters = []
    for i in graph_list:
        counter=0
        for j in i:
            print(j.getColor())
            for i in j.getconnections():
                print(i.id)
            if(j.getColor()=='gray' or j.getColor()=='black'):
                counter+=1
        counters.append(counter)
        print("")
    print(max(counters))

if __name__== '__main__':
    main()
