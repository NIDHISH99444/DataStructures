def path(matrix):
    dp=matrix[-1]
    for i in range(len(matrix)-2,-1,-1):
        for j in range(i+1):
            dp[j]=max(dp[j],dp[j+1])+matrix[i][j]
        print(dp)
    return dp[0]
A = [
  [468, 0],
  [335, 501]
]
print(path(A))