


def lengthOfLIS(nums,index,prevElement):
    if index == len(nums):
        return 0 
    
    # Case 1: Exclude current element
    exclude = lengthOfLIS(nums, index + 1, nums[prevElement])
    
    # Case 2: Include current element only if it is greater than the previous element
    include = 0
    if prevElement == -1 or nums[index] > nums[prevElement]:
        include = 1 + lengthOfLIS(nums, index + 1, nums[index])

    # Return the maximum of including and excluding current element
    return max(include, exclude)




nums = [-1,-2,-3,-4,-5,-6]

maxLength=0
prevElement=-10
index=0
print(lengthOfLIS(nums,index,prevElement))
