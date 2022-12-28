def isvalid(grid,visited,i,j):
    row=len(grid)
    col=len(grid[0])
    if i<0 or j<0 or i>=row or j>=col or visited[i][j]==1 or grid[i][j]==1:
        return False
    return True
def dfs(grid,visited,start):
    i,j = start[0],start[1]
    visited[i][j]=1
    sm = 0
    for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
        if isvalid(grid,visited,a+i,b+j):
            sm+=dfs(grid,visited,(a+i,b+j))
    return sm+1
if __name__ =='__main__':
    grid = [[0,1,0,0,0,0],[0,1,0,0,0,0],[1,0,1,0,1,1],[0,0,1,1,0,0],[1,0,0,1,0,0],[1,1,0,1,0,0]]
    row = len(grid)
    col = len(grid[0])
    visited = [[0]*col for i in range(row)]
    ans = []
    for i in range(row):
        for j in range(col):
            if visited[i][j]==0 and grid[i][j]==0:
                temp = dfs(grid,visited,(i,j))
                ans.append(temp)
    print(ans)