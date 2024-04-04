arr=[1 ,1 ,1 ,1]

target=4


def subsetSum(index, arr, target,dp):
    if index < 0 or target < 0:
        return False
    if target == 0:
        return True
    if dp[index][target] != -1:
        return dp[index][target]
    notTake = subsetSum(index - 1, arr, target, dp)
    take = False
    if arr[index] <= target:
        take = subsetSum(index - 1, arr, target - arr[index], dp)
    dp[index][target] = take or notTake
    return dp[index][target]
    
    

def subsetSumToK(target, arr):
    dp=[[-1 for i in range(target+1)]for j in range(len(arr)+1)]
    return subsetSum(len(arr)-1,arr,target,dp)




print(subsetSumToK(target, arr))