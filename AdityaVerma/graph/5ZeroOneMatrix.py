
board = [[0,0,0],[0,1,0],[1,1,1]]
       
def updateMatrix(grid):
    visited=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
    dist=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
    queue=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                visited[i][j]=1
                queue.append([i,j,0])
    while queue:
        rows=[-1,0,1,0]
        cols=[0,1,0,-1]
        i,j,distance=queue.pop(0)
        dist[i][j]=distance
        visited[i][j]=1
        for k in range(len(rows)):
            newr=i+rows[k]
            newc=j+cols[k]
            if newr>=0 and newr<len(grid) and newc>=0 and newc<len(grid[0]):
                if visited[newr][newc]==0:
                    queue.append([newr,newc,distance+1])
                    visited[newr][newc]=1
    return(dist)
        

print(updateMatrix(board))


