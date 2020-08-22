import  heapq
from  _collections import  defaultdict
def maxOccurance(arr,k):
    dict={}
    for ele in arr:
        if ele in dict:
            dict[ele]+=1
        else:
            dict[ele]=1
    print(dict)
    heap=[]
    for ele in dict:
        heapq.heappush(heap,(dict[ele],ele))
        if len(heap)>k:
            heapq.heappop(heap)
    res=[]
    while len(heap)>0:
        res.append(heapq.heappop(heap)[1])
    return (res)


arr=[3, 1, 4, 4, 5, 2, 6, 1]
k=2
print(maxOccurance(arr,k))
