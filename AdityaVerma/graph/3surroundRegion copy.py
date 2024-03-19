board = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]


def dfs(grid,i,j):
    grid[i][j]='D'
    rows=[-1,0,1,0]
    cols=[0,1,0,-1]
    for k in range(len(rows)):
        newr=i+rows[k]
        newc=j+cols[k]
        if newr>=0 and newr<len(grid) and newc>=0 and newc<len(grid[0]) and  grid[newr][newc]=="O":
            dfs(grid,newr,newc)
    
    
       
def surroundRegion( grid):
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i in (0,len(grid)-1) or j in (0,len(grid[0])-1)) and grid[i][j]=='O':
                dfs(grid,i,j)
        
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='D':
                grid[i][j]="O"
            else:
                grid[i][j]="X"
            
    return grid
        




print(surroundRegion(board))


