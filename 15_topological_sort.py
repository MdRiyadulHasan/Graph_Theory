from collections import deque
def kahn(graph,visited,indegree,q,res):
    for key in indegree:
        if indegree[key]==0:
            q.append(key)
            visited[key]=True
    while q:
        n = q.popleft()
        res.append(n)
        for child in graph[n]:
            if not visited[child]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
                    visited[child]=True
def represent_graph(edges,n):
    graph = {}
    visited = {}
    indegree = {}
    for i in range(1,n+1):
        graph[i] = []
        visited[i] = False
        indegree[i] = 0
    for u,v in edges:
        graph[u].append(v)
        indegree[v]+=1
    print(indegree)
    q = deque()
    res = []
    kahn(graph,visited,indegree,q,res)
    return res
if __name__ == '__main__':
    edges = [[1,2],[1,3],[1,7],[2,3],[4,3],[5,3],[6,3],[4,1],[6,1],[8,1],[9,7],[9,8]]
    n=9
    ans = represent_graph(edges,n)
    print(ans)
