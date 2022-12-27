from collections import deque
def bfs(graph,visited,q,res):
    q.append(1)
    visited[1] = True
    while q:
        n = q.popleft()
        res.append(n)
        for child in graph[n]:
            if not visited[child]:
                q.append(child)
                visited[child]=True
def graph_represent(edges,n):
    graph = {}
    visited = {}
    for i in range(1,n+1):
        graph[i]=[]
        visited[i] = False
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    res = []
    q = deque()
    bfs(graph,visited,q,res)
    return res

if __name__ == '__main__':
    edges = [[1,2],[1,6],[1,7],[1,8],[2,3],[3,6],[3,4],[3,5],[7,9],[8,9]]
    n = 9
    ans = graph_represent(edges,n)
    print(ans)