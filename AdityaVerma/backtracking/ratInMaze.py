n=4
maze=[[1, 0, 0, 0],[1, 1, 1, 1], [1, 1, 0, 0],[0, 1, 1, 1]]


def checkPath(maze,n,i,j,visited,res):
    if i==n-1 and j==n-1:
        return res
    visited[i][j]=1
    rows=[-1,0,1,0]
    cols=[0,1,0,-1]
    direction=['U','R','D','L']
    for k in range(len(rows)):
        newRow=i+rows[k]
        newCol=j+cols[k]
        newDir=direction[k]
        if newRow>=0 and newCol>=0 and newRow<n and newCol<n and maze[newRow][newCol]==1 and visited[newRow][newCol]==0:
            res+=newDir
            path=checkPath(maze,n,newRow,newCol,visited,res)
            if path:
                return path
    res=res[:-1]
    visited[i][j]=0




def findPath( maze, n):
    visited=[[0 for i in range(n)]for j in range(n)]
    res=""
    i,j=0,0
    return checkPath(maze,n,i,j,visited,res)


print(findPath(maze,n))
    