from collections import deque
def isvalid(grid,visited,x,y):
    row = len(grid)
    col = len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1:
        return False
    return True
def bfs(grid,visited,start,res,q):
    i = start[0]
    j=start[1]
    visited[i][j]=1
    q.append(start)
    while q:
        a,b=q.popleft()
        res.append(grid[a][b])
        for k,l in [[1,0],[-1,0],[0,1],[0,-1]]:
            if isvalid(grid,visited,a+k,b+l):
                q.append((a+k,b+l))
                visited[a+k][b+l]=1
if __name__ =='__main__':
    grid = [[3,1,5],[7,8,2],[14,11,9]]
    visited = [[0]*len(grid) for i in range(len(grid[0]))]
    res = []
    q = deque()
    bfs(grid,visited,(0,0),res,q)
    print(res)