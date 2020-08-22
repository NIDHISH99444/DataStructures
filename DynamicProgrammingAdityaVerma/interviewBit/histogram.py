

def bestTime(arr):
    min=arr[0]
    res=0
    for i in range(1,len(arr)):
        if arr[i]<min:
            min=arr[i]
        else:
            res=max(res,arr[i]-min)
    return res


arr=[7,1,5,3,6,4]
print(bestTime(arr))

