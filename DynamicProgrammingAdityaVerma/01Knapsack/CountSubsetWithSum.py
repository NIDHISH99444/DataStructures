

def countSubsetWithGivenSum(nums,sum):
    n=len(nums)+1
    t=[[0 for i in range(sum+1)] for j in range(n)]
    for i in range(len(t)):
        t[i][0]=1
    for i in range(1,len(t)):
        for j in range(1,len(t[0])):
            if nums[i-1]<=j:
                t[i][j]=t[i-1][j] + t[i-1][j-nums[i-1]]
            else:
                t[i][j]=t[i-1][j]
    print(t)
    return (t[-1][-1])

nums=[1,2,3,4,5]
sum=10
print(countSubsetWithGivenSum(nums,sum))
