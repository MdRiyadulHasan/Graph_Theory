def dfs(graph,node,visited,intime,outtime): 
    global timer
    intime[node]=timer 
    timer+=1
    visited[node]=True
    for child in graph[node]:
        if not visited[child]:
            dfs(graph,child,visited,intime,outtime)
    outtime[node]=timer
    timer+=1
def graph_represent(edges,n):
    graph = {}
    visited={}
    intime={}
    outtime={}
    for i in range(1,n+1):
        graph[i]=[]
        visited[i]=False
        intime[i]=None
        outtime[i]=None
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    dfs(graph,1,visited,intime,outtime)
    print(intime)
    print(outtime)
if __name__ == '__main__':
    n=8
    timer = 1
    edges = [[1,2],[1,3],[1,8],[2,4],[2,5],[2,6],[3,7]]
    graph_represent(edges,n)