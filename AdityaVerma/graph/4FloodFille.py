
board =  [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

def dfs(grid,i,j,color,oldColor):
    grid[i][j]=color
    rows=[-1,0,1,0]
    cols=[0,1,0,-1]
    for k in range(len(rows)):
        newr=i+rows[k]
        newc=j+cols[k]
        if newr>=0 and newr<len(grid) and newc>=0 and newc<len(grid[0]) and  grid[newr][newc]!=color and grid[newr][newc]==oldColor:
            dfs(grid,newr,newc,color,oldColor)
    
    
       
def floodFill(grid,sr,sc,color):
    
    oldColor=grid[sr][sc]
    if grid[sr][sc]!=color:
        dfs(grid,sr,sc,color,oldColor)

    return grid
            

            
        

print(floodFill(board,sr,sc,color))


