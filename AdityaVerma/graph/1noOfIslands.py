grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]



def dfs(visited,i,j):
    visited[newr][newc]=1
    rows=[-1,0,1,0]
    cols=[0,1,0,-1]
    for k in range(len(rows)):
        newr=i+rows[k]
        newc=j+cols[k]
        if newr>=0 and newr<len(grid) and newc>=0 and newc<len(grid[0]) and  grid[newr][newc]=="1" and visited[newr][newc]!=1:
            dfs(visited,newr,newc)
    
    
       
def numIslands( grid):
    visited=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1" and visited[i][j]!=1:
                count+=1
                dfs(visited,i,j)
            
            
    return count
        




print(numIslands(grid))


