def team(matrix):
    totalCnt=0
    for i in range(len(matrix)):
        cnt=0
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                cnt+=1
        if cnt>=2:
            totalCnt+=1

    return totalCnt


n=int(input())

matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))


print(team(matrix))