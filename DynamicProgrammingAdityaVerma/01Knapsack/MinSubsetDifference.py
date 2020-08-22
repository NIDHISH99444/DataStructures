from sys import maxsize
def subsetSum(nums, sum):
    n = len(nums) + 1
    t = [[0 for i in range(sum + 1)] for j in range(n)]
    for i in range(len(t)):
        t[i][0] = 1
    for i in range(1, len(t)):
        for j in range(1, len(t[0])):
            if nums[i - 1] <= j:
                t[i][j] = t[i - 1][j] or t[i - 1][j - nums[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return (t[-1])


def minAbsoluteDifference(nums):
    arr=subsetSum(nums, sum(nums))
    newArray=[]
    for i in range(len(arr)):
        if arr[i]==1:
            newArray.append(i)
    print(newArray)
    minDiff=maxsize
    for i in range(len(newArray)//2):
        minDiff=min(sum(nums)-2*newArray[i],minDiff)
    return minDiff





nums=[1,6,11,5]
print(minAbsoluteDifference(nums))
