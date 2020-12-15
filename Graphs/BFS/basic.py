import collections

def bfs(graph,root):
    visited,queue = set(),collections.deque([root])
    visited.add(root)
    while queue:
        currentNode = queue.popleft()

        for neighbour in graph[currentNode]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

gr = {0:[1,4],1:[0,2],2:[1,3,5],3:[2,4,5],4:[0,3,5],5:[0,2,3,4]}
bfs(gr,0)