from collections import deque
def bfs(graph,q,visited,distance,res):
    q.append(1)
    visited[1]=True
    distance[1]=0
    while q:
        n = q.popleft()
        res.append(n)
        for child in graph[n]:
            if not visited[child]:
                visited[child]=True
                q.append(child)
                distance[child]=distance[n]+1
def graph_represent(edges,n):
    graph = {}
    visited = {}
    distance = {}
    for i in range(1,n+1):
        graph[i]=[]
        visited[i] = False
        distance[i] = None
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    q = deque()
    res = []
    bfs(graph,q,visited,distance,res)
    print(res)
    return distance
if __name__ == '__main__':
    edges = [[1,2],[1,6],[1,7],[1,8],[2,3],[3,6],[3,4],[3,5],[7,9],[8,9]]
    n = 9
    ans = graph_represent(edges,n)
    print(ans)