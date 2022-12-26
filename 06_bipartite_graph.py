def bipartite(graph,node,visited,color,c):
    color[node]=c
    visited[node]=1
    for child in graph[node]:
        if not visited[child]:
            temp = bipartite(graph,child,visited,color,c^1)
            if temp==False:
                return False
        else:
            if color[node]==color[child]:
                return False
    return True

def graph_represent(edges,n):
    graph = {}
    visited = {}
    color = {}
    for i in range(1,n+1):
        graph[i] = []
        visited[i]=0
        color[i]=None
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    temp = bipartite(graph,1,visited,color,0)
    print(temp)
if __name__ == '__main__':
    edges = [[1,2],[1,4],[2,3],[3,6],[6,5],[4,5]]
    n=6
    graph_represent(edges,n)