arr=[2]

target=3


def coinChange(index, arr, target,dp):
    if index == 0:
        if target%arr[index]==0:
            return target//arr[index]   
         
            return -1
    if dp[index][target]!=-1:
        return dp[index][target]
    notTake = coinChange(index - 1, arr, target, dp)
    take = 100
    if arr[index] <= target:
        take = 1+coinChange(index, arr, target - arr[index], dp)
    dp[index][target]= min(take, notTake)
    return dp[index][target]
    
    

def coinChange1(target, arr):
     





print(coinChange1(target, arr))




    def coinChangeHelper(self,index,arr, target, dp):
        if index == 0:
            if target%arr[index]==0:
                return target//arr[index]   
            return float('inf')
        
        if dp[index][target]!=-1:
            return dp[index][target]
        notTake = self.coinChangeHelper(index - 1, arr, target, dp)
        take = 100
        if arr[index] <= target:
            take = 1+self.coinChangeHelper(index, arr, target - arr[index], dp)
        dp[index][target]= min(take, notTake)
        return dp[index][target]
        

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [[-1 for i in range(amount+1)]for j in range(len(coins)+1)]
        return self.coinChangeHelper(len(coins)-1,coins,amount,dp)
        return -1 if result == float('inf') else result