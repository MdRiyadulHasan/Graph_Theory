import heapq
def dijkstra(graph,start,visited,distance):
    nums = []
    distance[start]=0
    heapq.heappush(nums,[0,start])
    while nums:
        d,n=heapq.heappop(nums)
        visited[n]=1
        for cd,cn in graph[n]:
            if not visited[cn] and distance[n]+cd<distance[cn]:
                distance[cn]=distance[n]+cd
                heapq.heappush(nums,[distance[n]+cd,cn])
    print(distance)

def graph_represent(edges,n):
    graph = {}
    visited = {}
    distance = {}
    for i in range(1,n+1):
        graph[i]=[]
        distance[i]=float('inf')
        visited[i]=0
    for u,v,d in edges:
        graph[u].append([d,v])
    start = 1
    dijkstra(graph,start,visited,distance)


if __name__=='__main__':
    edges = [[1,3,2],[1,2,1],[2,3,1],[3,4,2],[2,5,1],[5,4,1]]
    n = 5
    graph_represent(edges,n)