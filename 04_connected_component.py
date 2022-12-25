def dfs(graph,node,visited):
    print(node)
    visited.add(node)
    c = 0
    for child in graph[node]:
        if child not in visited:
            c+=dfs(graph,child,visited)
    return c+1
def graph_represent(edges,nodes):
    graph = {}
    for key in nodes:
        graph[key]=[]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited=set()
    ans = []
    for node in nodes:
        if node not in visited:
            temp = dfs(graph,node,visited)
            ans.append(temp)
    return ans

if __name__ == '__main__':
    edges = [['A','B'],['A','C'],['A','D'],['B','E'],['D','E'],['F','G'],['F','H'],['I','J']]
    nodes=['A','B','C','D','E','F','G','H','I','J','K']
    ans = graph_represent(edges,nodes)
    print(ans)