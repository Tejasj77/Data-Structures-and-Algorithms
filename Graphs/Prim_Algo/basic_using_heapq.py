'''
This Prim's Algorithm Code is for finding weight of minimum spanning tree
of a connected graph.
For argument graph, it should be a dictionary type
such as
graph = {
    'a': [ [3, 'b'], [8,'c'] ],
    'b': [ [3, 'a'], [5, 'd'] ],
    'c': [ [8, 'a'], [2, 'd'], [4, 'e'] ],
    'd': [ [5, 'b'], [2, 'c'], [6, 'e'] ],
    'e': [ [4, 'c'], [6, 'd'] ]
}
where 'a','b','c','d','e' are nodes (these can be 1,2,3,4,5 as well)
'''

import heapq  # for priority queue


# prim's algo. to find weight of minimum spanning tree
def prims_minimum_spanning(graph_used):
    vis = []
    s = [[0, 'a']]
    prim = []
    mincost = 0

    while (len(s) > 0):
        v = heapq.heappop(s)
        x = v[1]
        if (x in vis):
            continue

        mincost += v[0]
        prim.append(x)
        vis.append(x)

        for j in graph_used[x]:
            i = j[-1]
            if (i not in vis):
                heapq.heappush(s, j)
                print(s)

    return mincost
graph = {
    'a': [ [3, 'b'], [8,'c'] ],
    'b': [ [3, 'a'], [5, 'd'] ],
    'c': [ [8, 'a'], [2, 'd'], [4, 'e'] ],
    'd': [ [5, 'b'], [2, 'c'], [6, 'e'] ],
    'e': [ [4, 'c'], [6, 'd'] ]
}
g1 = {
    'a':[[5,'e'],[2,'d'],[6,'c']],
    'b':[[1,'c'],[3,'e']],
    'c':[[4,'d'],[6,'a'],[1,'b']],
    'd':[[2,'a'],[4,'c']],
    'e':[[5,'a'],[3,'b']]
}
print(prims_minimum_spanning(graph))
print(prims_minimum_spanning(g1))