def represent(values,n):
    graph = {}
    for i in range(n):
        graph[i]=[]
    print(graph)
    for (u,v) in values:
        graph[u].append(v)
        graph[v].append(u)
    return graph
if __name__ =='__main__':
    values = [[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]
    n = 6
    ans = represent(values,n)
    print(ans)