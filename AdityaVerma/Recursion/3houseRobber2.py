def houseRobbery(arr,index,dp):
    if index==0:
        return arr[index]
    if index<0:
        return 0 
    if dp[index]!=-1:
        return dp[index]

    res1=arr[index]+houseRobbery(arr,index-2,dp)
    res2=houseRobbery(arr,index-1,dp)
    dp[index]=max(res1,res2)
    return dp[index]
    



arr=[1]
arr1=arr[:len(arr)-1]
dp=[-1]*len(arr1)
arr2=arr[1:len(arr)]
dp1=[-1]*len(arr2)
print(houseRobbery(arr1,len(arr1)-1,dp))
print(houseRobbery(arr2,len(arr2)-1,dp1))