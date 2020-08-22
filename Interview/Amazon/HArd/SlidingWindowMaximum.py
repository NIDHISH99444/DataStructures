
from _collections import deque
def slidingWindow(arr,k):
    q=deque()
    res=[]
    for i in range(k):
        while q:
            if arr[q[-1]]<arr[i]:
                q.pop()
            else:
                break
        q.append(i)

    for i in range(k,len(arr)):
        res.append(arr[q[0]])
        if (i-k) in q:
            q.popleft()
        while q:
            if arr[q[-1]]<arr[i]:
                q.pop()
            else:
                break
        q.append(i)
    res.append(arr[q[0]])
    return res

arr=[7,2,4]
k = 2


print(slidingWindow(arr,k))