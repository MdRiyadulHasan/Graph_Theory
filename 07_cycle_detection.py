def detect_cycle(graph,node,visited,par):
    visited[node]=True
    for child in graph[node]:
        if not visited[child]:
            return detect_cycle(graph,child,visited,node)
        else:
            if child !=par:
                return True
    return False
def graph_represent(edges,n):
    graph = {}
    visited={}
    for i in range(1,n+1):
        graph[i]=[]
        visited[i]=False
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    temp = detect_cycle(graph,1,visited,-1)
    print(temp)

if __name__ == '__main__':
    n=5
    edges = [[1,2],[1,3],[1,5],[2,3],[2,4],[4,5]]
    graph_represent(edges,n)