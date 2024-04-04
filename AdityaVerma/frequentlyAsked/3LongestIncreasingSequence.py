
def findIndex(arr,ele):
    start=0
    end=len(arr)-1
    resIndex=-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            res=mid
            end=mid-1
        else:
            start=mid+1
    return res


def lengthOfLIS(nums):
    res=[]
    for i in range(len(nums)):
        if i==0:
            res.append(nums[i])
        elif len(res) and  nums[i]>res[-1] :
            res.append(nums[i])
        else:
            index=findIndex(res,nums[i])
            print("before",res)
            res[index]=nums[i]
            print("after",res)
    return len(res)


arr=[4,10,4,3,8,9]
print(lengthOfLIS(arr))

