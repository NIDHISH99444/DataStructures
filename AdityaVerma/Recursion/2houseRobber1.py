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
    




arr=[2,7,9,3,1]
dp=[-1]*len(arr)
print(houseRobbery(arr,len(arr)-1,dp))