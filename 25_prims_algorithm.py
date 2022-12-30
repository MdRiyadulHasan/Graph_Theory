import heapq
def prims(graph,start,parent,visited,distance):
    nums = []
    heapq.heappush(nums,[0,start])
    distance[start]=0
    parent[start]=-1
    while nums:
        d,n = heapq.heappop(nums)
        if not visited[n]:
            visited[n]=1
            for cd,cn in graph[n]:
                if distance[cn]>cd and not visited[cn]:
                    parent[cn]=n
                    distance[cn]=cd
                    heapq.heappush(nums,[cd,cn])
    print(distance)
    print(parent)

def represent_graph(edges,n):
    graph = {}
    parent = {}
    distance = {}
    visited = {}
    for i in range(1,n+1):
        graph[i]=[]
        parent[i] = None
        visited[i]=0
        distance[i] = float('inf')
    for u,v,d in edges:
        graph[u].append([d,v])
        graph[v].append([d,u])
    start = 1
    prims(graph,start,parent,visited,distance)
    
if __name__ =='__main__':
    edges = [[1,2,1],[1,5,3],[2,5,2],[2,4,1],[2,3,4],[5,4,2],[4,3,1]]
    n = 5
    represent_graph(edges,n)