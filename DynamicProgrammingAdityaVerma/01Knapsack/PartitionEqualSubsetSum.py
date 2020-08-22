def subsetSum(nums,sum):
    n=len(nums)+1
    t=[[False for i in range(sum+1)] for j in range(n)]
    for i in range(len(t)):
        t[i][0]=True
    for i in range(1,len(t)):
        for j in range(1,len(t[0])):
            if nums[i-1]<=j:
                t[i][j]=t[i-1][j] or t[i-1][j-nums[i-1]]
            else:
                t[i][j]=t[i-1][j]

    return (t[-1][-1])

def canPartition( nums):
    arrSum=sum(nums)
    if arrSum%2!=0:
        return False
    return subsetSum(nums,arrSum//2)




nums=[1,5,11,5]
if canPartition(nums):
    print("true")
else:
    print("false")
