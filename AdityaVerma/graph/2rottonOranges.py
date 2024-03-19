grid = [[2,1,1],[1,1,1],[0,1,2]]


def rottonOranges(grid):
    visited=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    queue=[]
    countFresh=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==2:
                visited[i][j]=2
                queue.append([i,j,0])
            elif grid[i][j]==1:
                countFresh+=1
    rows=[-1,0,1,0]
    cols=[0,1,0,-1]
    maxTime=0
    cnt=0
    while queue:
        indexI,indexJ,time=queue.pop(0)
        maxTime=max(maxTime,time)
        for i in range(len(rows)):
            nextrow=indexI+rows[i]
            nextcol=indexJ+cols[i]
            if nextrow>=0 and nextrow<len(grid) and nextcol>=0 and nextcol<len(grid[0]): 
                if grid[nextrow][nextcol]==1 and visited[nextrow][nextcol]!=2:
                    visited[nextrow][nextcol]=2 
                    queue.append((nextrow,nextcol,time+1))
                    cnt+=1
        print(queue)
    print(visited)
    if cnt==countFresh:
        return maxTime
    else:
        return -1 
            



    



print(rottonOranges(grid))