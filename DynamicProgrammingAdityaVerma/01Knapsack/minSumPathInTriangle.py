def pathSum(A):
    dp=A[-1]
    for i in range(len(A)-2,-1,-1):
        for j in range(i+1):
            dp[j]=A[i][j]+min(dp[j],dp[j+1])

    return dp[0]
A=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(pathSum(A))