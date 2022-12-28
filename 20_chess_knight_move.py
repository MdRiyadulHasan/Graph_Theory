from collections import deque
def isvalid(grid,visited,i,j):
    row = len(grid)
    col = len(grid[0])
    if i<0 or j<0 or i>=row or j>=col or visited[i][j]==1:
        return False
    return True
def bfs(grid,visited,distance,start,end):
    i,j=start[0],start[1]
    visited[i][j]=1
    distance[i][j]=0
    q=deque()
    q.append((i,j))
    while q:
        a,b = q.popleft()
        for k,l in [[2,1],[-2,1],[-1,2],[1,2],[2,-1],[-2,-1],[-1,-2],[1,-2]]:
            if isvalid(grid,visited,a+k,b+l):
                q.append((a+k,b+l))
                visited[a+k][b+l]=1
                distance[a+k][b+l]=1+distance[a][b]


if __name__ =='__main__':
    grid = [['','B','',''],['','','',''],['','A','',''],['','','',''],['','','','']]
    row = len(grid)
    col = len(grid[0])
    visited=[[0]*col for i in range(row)]
    distance = [[-1]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='A':
                start=(i,j)
            if grid[i][j]=='B':
                end = (i,j)
    bfs(grid,visited,distance,start,end)
    print(distance[end[0]][end[1]])
            