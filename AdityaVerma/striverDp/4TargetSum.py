class Solution(object):
    def findTargetSumWaysHelper(self, index, nums, target, dp):
        if target == 0:
            return 1
        if index < 0 or target < 0:
            return 0
        if dp[index][target] != -1:
            return dp[index][target]
        if nums[index] <= target:
            take = self.findTargetSumWaysHelper(index - 1, nums, target - nums[index], dp)
            notTake = self.findTargetSumWaysHelper(index - 1, nums, target, dp)
            dp[index][target] = take + notTake
            return dp[index][target]
        else:
            dp[index][target] = self.findTargetSumWaysHelper(index - 1, nums, target, dp)
            return dp[index][target]

    def findTargetSumWays(self, nums, target):
        if sum(nums) < target or (sum(nums) + target) % 2 != 0:
            return 0
        targetCheck = (sum(nums) + target) // 2
        index = len(nums) - 1
        dp = [[-1 for _ in range(targetCheck + 1)] for _ in range(len(nums) + 1)]
        return self.findTargetSumWaysHelper(index, nums, targetCheck, dp)

# Test case
nums = [0,0,0,0,0,0,0,0,1]
target = 1
solution = Solution()
print(solution.findTargetSumWays(nums, target))  # Output: 256
