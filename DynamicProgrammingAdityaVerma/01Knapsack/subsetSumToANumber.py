def countSubsetWithGivenSum(nums,sum):
    n=len(nums)+1
    t=[[0 for i in range(sum+1)] for j in range(n)]
    print(t)

    for i in range(len(t[0])):
        t[0][i]=False

    for i in range(len(t)):
        t[i][0] = True

    for i in range(1,len(t)):
        for j in range(1,len(t[0])):
            if nums[i-1]<=j:
                t[i][j]=t[i-1][j] or  t[i-1][j-nums[i-1]]
            else:
                t[i][j]=t[i-1][j]
    print(t)
    return (t[-1][-1])

nums=[1,3,7]
sum=4
print(countSubsetWithGivenSum(nums,sum))
