def represent(values,n):
    M = [[0]*n for _ in range(n)]
    print(M)
    for (u,v)in values:
        M[u][v]=1
        M[v][u]=1
    return M

if __name__ =='__main__':
    values = [[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]
    n = 6
    ans = represent(values,n)
    print(ans)