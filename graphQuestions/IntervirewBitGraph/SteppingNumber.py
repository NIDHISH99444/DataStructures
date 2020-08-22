def dfs(n,m,stepNum):
    if stepNum<=m and stepNum>=n:
        print(stepNum)
    if  stepNum==0 or stepNum>m:
        return
    lastDigit=stepNum%10
    stepNumA=stepNum*10+(lastDigit-1)
    stepNumB = stepNum * 10 + (lastDigit + 1)
    if lastDigit==0:
        dfs(n,m,stepNumB)
    elif lastDigit==9:
        dfs(n,m,stepNumA)
    else:
        dfs(n,m,stepNumA)
        dfs(n, m, stepNumB)
def displayStepping(n,m):
    for i in range(10):
        dfs(n,m,i)

n,m=0,100
displayStepping(n,m)