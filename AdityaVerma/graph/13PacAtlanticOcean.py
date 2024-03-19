heights = [[2,1],[1,2]]
def dfs(i,j,visit,prevHeight,height):
    rows=[-1,0,1,0]
    cols=[0,1,0,-1]
    visit.add((i,j))
    for k in range(len(rows)):
        newR=i+rows[k]
        newC=j+cols[k]
        if newR>=0 and newR<len(height) and newC>=0 and newC<len(height[0]) and prevHeight<=height[newR][newC] and (newR,newC) not in visit:
            visit.add((newR,newC))
            dfs(newR,newC,visit,height[newR][newC],height)

def pacificAtlantic( height):
    
    visitedPac=set()
    visitedAtl=set()
    
    for i in range(len(height[0])):
        dfs(0,i,visitedPac,height[0][i],height)
        dfs(len(height)-1,i,visitedAtl,height[len(height)-1][i],height)

    for i in range(len(height)):
        dfs(i,0,visitedPac,height[i][0],height)
        dfs(i,len(height[0])-1,visitedAtl,height[i][len(height[0])-1],height)
    
    
    res=[]
    for i in range(len(height)):
        for j in range(len(height[0])):
            if (i,j) in visitedAtl and (i,j) in visitedPac:
                res.append((i,j))
    return res





print(pacificAtlantic( heights))

