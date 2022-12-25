def dfs(graph,node,visited=set()):
    print(node)
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph,child,visited)
def graph_represent(values,n):
    graph = {}
    for i in range(1,n+1):
        graph[i] = []
    for u,v in values:
        graph[u].append(v)
        graph[v].append(u)
    dfs(graph,1)
    return graph

if __name__ == '__main__':
    values = [[1,2],[1,5],[2,5],[2,4],[2,3],[3,4],[4,5],[3,6],[4,6],[5,6]]
    n=6
    ans = graph_represent(values,n)
    print(ans)