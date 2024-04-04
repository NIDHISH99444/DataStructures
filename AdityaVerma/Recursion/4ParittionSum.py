nums = [1,5,10,5]

def checkSum(nums, index, target,dp):
    if index < 0:
        return False
    if target == 0:
        return True
    if dp[index][target]!=-1:
        return dp[index][target]
    if nums[index] <= target:
        res1 = checkSum(nums, index - 1, target - nums[index],dp)
        res2 = checkSum(nums, index - 1, target,dp)
        dp[index][target]= res1 or res2
        return dp[index][target]
    else: 
        dp[index][target]=checkSum(nums, index - 1, target,dp)
        return dp[index][target]


def canPartition( nums):
    target_sum = sum(nums) // 2
    print(target_sum)
    n=len(nums)+1
    m=target_sum+1
    dp=[[-1 for i in range(m)]for j in range(n)]
    return checkSum(nums, len(nums) - 1, target_sum,dp)




print(canPartition( nums))
    



