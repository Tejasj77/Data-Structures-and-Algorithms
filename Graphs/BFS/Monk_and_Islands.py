from collections import defaultdict
from pythonds.graphs import Graph,Vertex
from collections import deque as Queue
import inspect
souce  = inspect.getsource(Graph)

"""

"""

def bfs(g,start):
    counter = 0
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.append(start)
    while vertQueue:
        currentvert = vertQueue.popleft()
        for nbr in currentvert.getConnections():
            if(nbr.getColor() == 'white'):
                nbr.setColor('gray')
                counter = currentvert.getDistance() + 1
                nbr.setDistance(currentvert.getDistance() + 1)
                nbr.setPred(currentvert)
                vertQueue.append(nbr)
        currentvert.setColor('black')

    return counter


t = 1

m = []
file = open("monk.txt","r")
for _ in range(1):

    g = Graph()
    nodes, edgelist = [int(i) for i in input().split()]

    edgedata = [input().split() for _ in range(edgelist)]
    print(edgedata[0][0])
    for i in edgedata:
        #print('Add edge between {} and {}'.format(int(i[0]), int(i[1])))
        g.addEdge(int(i[0]), int(i[1]))
        g.addEdge(int(i[1]), int(i[0]))
    ans1 = bfs(g, g.getVertex(int(edgedata[0][0])))
    m.append(ans1)
    nodes,edgelist,edgedata = None,None,None

for i in m:
    print(i)


