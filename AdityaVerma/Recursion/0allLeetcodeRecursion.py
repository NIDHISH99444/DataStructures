#print all arrays with sum as 2 
#ouptut=[[2],[1,1]]

input=[1,2,1]
sum=2

def checkSum(input,output,sum,allResult):
    if sum==0:
        allResult.append(output[:])
        return
         
    if len(input)==0:
        return 
    
    checkSum(input[1:],output,sum,allResult)
    checkSum(input[1:],output+[input[0]],sum-input[0],allResult)      #

output=[]
allResult=[]
checkSum(input,output,sum,allResult)
print(allResult)

#print the first  arrays with sum as 2 

def checkSum(input, output, target):
    if target == 0:
        return output[:]
    if len(input) == 0:
        return None

    res = checkSum(input[1:], output, target)
    if res is not None:
        return res
    return checkSum(input[1:], output + [input[0]], target - input[0])

input = [1, 2, 1]
target = 2
result = checkSum(input, [], target)
print(result)  # Output: [2]



#Combinations:


def combine(self, n, k):
    res = []
    self.dfs(range(1, n + 1), k, 0, [], res)
    return res


def dfs(self, nums, k, index, path, res):
    # if k < 0:  #backtracking
    # return
    if k == 0:
        res.append(path)
        return  # backtracking
    for i in range(index, len(nums)):
        self.dfs(nums, k - 1, i + 1, path + [nums[i]], res)


#PermutationsI


class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


#PermutationsII


def permuteUnique(self, nums):
    res, visited = [], [False] * len(nums)
    nums.sort()
    self.dfs(nums, visited, [], res)
    return res


def dfs(self, nums, visited, path, res):
    if len(nums) == len(path):
        res.append(path)
        return
    for i in range(len(nums)):
        if not visited[i]:
            if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:  # here should pay attention
                continue
            visited[i] = True
            self.dfs(nums, visited, path + [nums[i]], res)
            visited[i] = False


#Subsets1


def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res


def dfs(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        self.dfs(nums, i + 1, path + [nums[i]], res)


#SubsetsII


def subsetsWithDup(self, nums):
    res = []
    nums.sort()
    self.dfs(nums, 0, [], res)
    return res


def dfs(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        self.dfs(nums, i + 1, path + [nums[i]], res)


# Combination Sum


def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res


def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


# CombinationSumII


def combinationSum2(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res


def dfs(self, candidates, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return  # backtracking
    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i - 1]:
            continue
        self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)