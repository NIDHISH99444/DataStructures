import heapq
def findingMissingPositive(arr):
    arr=list(set(arr))
    print(arr)

    heap=[]
    for i in range(len(arr)):
        if arr[i]>0:
            heapq.heappush(heap,arr[i])
    val=1
    while len(heap)>0:
        if heapq.heappop(heap)!=val:
            return val
        else:
            val+=1
    return val

arr=[0,1,2]
arr=[3,4,-1,1]
arr=[7,8,9,11,12]
arr=[0,2,2,1,1]
print(findingMissingPositive(arr))
