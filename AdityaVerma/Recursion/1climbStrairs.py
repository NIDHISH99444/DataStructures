def countStairs(n,dp):
    if n==0:
        return 1
    if n<0:
        return 0
        return 0 
    if dp[n]!=-1:
        return dp[n]

    res1=countStairs(n-1,dp)
    res2=countStairs(n-2,dp)
    dp[n]=res1+res2
    return dp[n]
    



n=4
dp=[-1]*(n+1)
print(countStairs(n,dp))