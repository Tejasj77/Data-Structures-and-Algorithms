from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s, l):
        #dist = [0] * 10000000
        dist = [0] * 10
        #visited = [False] * 10000000  # (len(self.graph)+1)
        visited = [False]*10
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i] == False:
                    dist[i] = dist[s] + 1  # this is the dist list
                    queue.append(i)
                    visited[i] = True
        print(l)
        print(visited)
        print(dist)
        return dist[l[0]]


def main():
    t = int(input())
    ml = []
    for i in range(t):
        l = list(map(int, input().split()))
        g = Graph()
        for i in range(l[1]):
            l2 = list(map(int, input().split()))
            g.addEdge(l2[0], l2[1])
            #g.addEdge(l2[1], l2[0]) # graph is bidirectional
        ans = g.BFS(1, l)
        ml.append(ans)
    for i in ml:
        print(i)


main()
