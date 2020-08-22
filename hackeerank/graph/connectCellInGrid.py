def matrixCheck(matrix,i,j,cnt):
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]==0:
        return
    matrix[i][j]=0
    cnt[0]+=1
    dx=[-1,-1,0,1,1,1,0,-1,-1]
    dy=[ 0,1,1,1,0,-1,-1,-1,0]
    for s in range(len(dx)):
        matrixCheck(matrix,i+dx[s],j+dy[s],cnt)
def connectCell(matrix):
    cnt=[0]
    maxCount=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                matrixCheck(matrix,i,j,cnt)
                print(cnt[0])
                maxCount=max(maxCount,cnt[0])
                cnt[0]=0
    return maxCount



matrix=[
[1 ,1 ,0 ,0],
[0, 1 ,1 ,0],
[0, 0 ,1 ,0],
[1 ,0, 0 ,0]]

print(connectCell(matrix))