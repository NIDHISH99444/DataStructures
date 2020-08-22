from _collections import deque
def check(matrix,i,j):
    q=deque()
    step=1
    q.append((i,j,step))
    matrix[i][j]='0'
    while q:
        i,j,step=q.popleft()
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        for s in range(4):
            if i+dx[s]<0 or i+dx[s]>=len(matrix) or j+dy[s]<0 or j+dy[s]>=len(matrix[0]) or matrix[i+dx[s]][j+dy[s]]=='0':
                continue

            if matrix[i+dx[s]][j+dy[s]]=='d':
                return step
            q.append((i+dx[s],j+dy[s],step+1))
            matrix[i + dx[s]][j + dy[s]] = '0'
def checkPath(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='s':
                val=check(matrix,i,j)
                if val!=None:
                    return val
                else:
                    return -1
grid=\
[['#', '0', '#', 's'],
['0', '#', '#', '0'],
['0', '0', '#', '*'],
['0', 'd', '*', '*']]

print(checkPath(grid))