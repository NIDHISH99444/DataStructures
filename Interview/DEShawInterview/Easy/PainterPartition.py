def checkPainter(arr,k,mid):
    i=0
    total=1
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum>mid:
            sum=arr[i]
            total+=1
            if total>k:
                return False
    return True

#print(checkPainter([10,20,30,40],2,60))

def paniterPartition(arr,k):
    start=min(arr)
    end=sum(arr)
    ans=-1
    while start<=end:
        mid=start+(end-start)//2
        if checkPainter(arr,k,mid):
            ans=mid
            end=mid-1
        else:
            start=mid+1
    return ans





print(paniterPartition([10,20,30,40],2))