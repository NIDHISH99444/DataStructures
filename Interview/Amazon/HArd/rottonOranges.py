
from _collections import deque

def update(grid,x,y,steps,q):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for i in range(4):
        if x+dx[i]<0 or x+dx[i]>=len(grid) or y+dy[i]<0 or y+dy[i]>=len(grid[0]) or grid[x+dx[i]][y+dy[i]] ==2 or  grid[x+dx[i]][y+dy[i]]==0:
            continue
        else:
            grid[x+dx[i]][y+dy[i]]=2
            q.append((steps+1,x+dx[i],y+dy[i]))


def checkOranges(grid):
    steps=0
    q=deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==2:
                q.append((steps,i,j))
    print(q)
    while q:
        steps,i,j=q.popleft()
        update(grid,i,j,steps,q)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                return -1
    return steps

grid=[[2,1,1],[1,1,0],[0,1,1]]
print(checkOranges(grid))