def find(graph,node):
    if graph[node]<0:
        return node
    else:
        return find(graph,graph[node])       
def union(graph,a,b):
    ta =a 
    tb = b
    a = find(graph,a)
    b = find(graph,b)
    if a==b:
        print('can not connect, same family ',ta ,tb)
    else:
        if graph[a]<graph[b]:
            graph[a]=graph[a]+graph[b]
            graph[b]=a
        else:
            graph[b]=graph[a]+graph[b]
            graph[a]=b
def represent_graph(edges,n):
    graph ={}
    for i in range(n):
        graph[i]=-1
    for u,v in edges:
        union(graph,u,v)   
if __name__ == '__main__':
    edges = [[0,1],[1,2],[2,3],[4,5],[1,3]]
    n=7
    represent_graph(edges,n)