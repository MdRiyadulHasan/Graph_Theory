def graph_represent(edges,n):
    graph = {}
    for i in range(1,n+1):
        graph[i]=[]
    for u,v,d in edges:
        graph[u].append([d,v])
        graph[v].append([d,u])
    print(graph)
if __name__ == '__main__':
    edges = [[1,2,3],[1,3,2],[3,4,4],[2,5,1],[3,7,4],[4,7,5],[4,5,8],[5,6,6],[6,7,2],[6,9,1],[7,9,2],[7,8,1]]
    n=9
    graph_represent(edges,n)    