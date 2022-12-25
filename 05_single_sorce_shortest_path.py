def single_s_s_path(graph,node,d,distance,par):
    distance[node]=d
    for child in graph[node]:
        if child!=par:
            single_s_s_path(graph,child,distance[node]+1,distance,node)

def graph_represent(edges,nodes):
    graph = {}
    distance = {}
    for key in nodes:
        graph[key]=[]
        distance[key]=None
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    start = 'A'
    #distance[start]=0
    single_s_s_path(graph,start,0,distance,-1)
    for key,val in distance.items():
        print(key, val)

if __name__ =='__main__':
    edges = [['A','B'],['B','D'],['D','G'],['G','H'],['G','I'],['A','C'],['C','E'],['C','F']]
    nodes = ['A','B','C','D','E','F','G','H','I']
    graph_represent(edges,nodes)