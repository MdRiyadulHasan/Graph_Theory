def isvalid(grid,visited,i,j):
    row = len(grid)
    col = len(grid[0])
    if i<0 or j<0 or i>=row or j>=col or visited[i][j]==1:
        return False
    return True
def dfs(grid,visited,start,res):
    i,j = start[0],start[1]
    res.append(grid[i][j])
    visited[i][j]=1
    if isvalid(grid,visited,i,j+1):
        dfs(grid,visited,(i,j+1),res)
    if isvalid(grid,visited,i,j-1):
        dfs(grid,visited,(i,j-1),res)
    if isvalid(grid,visited,i+1,j):
        dfs(grid,visited,(i+1,j),res)
    if isvalid(grid,visited,i-1,j):
        dfs(grid,visited,(i-1,j),res)


if __name__ =='__main__':
    grid = [[3,1,5],[7,8,2],[14,11,9]]
    visited = [[0]*len(grid) for i in range(len(grid[0]))]
    start = (0,0)
    res = []
    dfs(grid,visited,start,res)
    print(res)