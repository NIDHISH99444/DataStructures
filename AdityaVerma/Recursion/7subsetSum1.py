
def dfs(nums,sum,list1,index):
    if index==len(nums):
        list1.append(sum)
        return
    dfs(nums[index+1:],sum+nums[index],list1,index)
    dfs(nums[index+1:],sum,list1,index)
        
def subsetSums( arr, N):
    # code here
    list1=[]
    dfs(arr,0,list1,0)
    list1.sort()
    return list1



arr=[2,3]
N=2
print(subsetSums(arr, N))
