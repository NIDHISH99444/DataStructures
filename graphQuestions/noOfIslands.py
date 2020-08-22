
def dfs(graph,i,j,cnt):
    if i<0 or i>=len(graph) or j<0 or j>=len(graph[0]) or graph[i][j]==0:
        return
    if graph[i][j]==1:
        graph[i][j]=0
        cnt[0]+=1
    rowNbr = [-1, 0,1, 0]
    colNbr = [0, 1 ,0, -1]
    for s in range(len(rowNbr)):
        dfs(graph,i+rowNbr[s],j+colNbr[s],cnt)

def noOfIslands(graph):
    maxVal=0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]==1:
                cnt=[0]
                dfs(graph,i,j,cnt)
                maxVal=max(cnt[0],maxVal)
    return maxVal
graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

print(noOfIslands(graph))