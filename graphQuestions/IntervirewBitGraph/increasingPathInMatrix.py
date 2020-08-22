def solve( A):
    m = len(A)
    n = len(A[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    if m == 1 and n == 1:
        return 1

    dp[0][0] = 1

    for i in range(1, m):
        if A[i][0] > A[i - 1][0]:
            dp[i][0] = 1 + dp[i - 1][0]
        else:
            break

    for j in range(1, n):
        if A[0][j] > A[0][j - 1]:
            dp[0][j] = 1 + dp[0][j - 1]
        else:
            break

    for i in range(1, m):
        for j in range(1, n):

            if A[i][j] > A[i - 1][j] and dp[i-1][j]!=0:
                dp[i][j]=dp[i-1][j]+1

            if  A[i][j] > A[i][j - 1] and dp[i][j-1]!=0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1]+1)

    if dp[-1][-1] == 0:
        return -1
    else:
        return dp[-1][-1]


A = [  [1, 2, 3, 4],
        [2, 2, 3, 4],
        [3, 2, 3, 4],
        [4,5,6,7]
     ]

print(solve(A))