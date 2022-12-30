def find(graph, node):
    if graph[node]<0:
        return node
    else:
        return find(graph,graph[node])
def union(graph,a,b,ans):
    ta,tb=a,b
    a = find(graph,a)
    b = find(graph,b)
    if a==b:
        pass
    else:
        ans.append([ta,tb])
        if graph[a]<graph[b]:
            graph[a]=graph[a]+graph[b]
            graph[b]=a
        else:
            graph[b] = graph[a]+graph[b]
            graph[a]=b
def graph_represent(edges,n):
    graph ={}
    for i in range(1,n+1):
        graph[i]=-1
    ans = []
    for u,v,d in edges:
        union(graph,u,v,ans)
    print(ans)
if __name__ == '__main__':
    edges = [[1,2,1],[1,3,3],[3,6,2],[2,6,4],[6,7,2],[6,5,6],[7,5,7],[3,4,1],[4,5,5]]
    n = 7
    edges = sorted(edges, key = lambda edges:edges[2])
    graph_represent(edges,n)
    