from heapq import heappush,heappop
def minRooms(intervals):
    intervals.sort(key=lambda x : x[0])
    heap=[]
    maxRooms=1
    heappush(heap, intervals[0][1])
    for i in range(1,len(intervals)):
        k = heappop(heap)
        if intervals[i][0]<k:
            heappush(heap,k)
            heappush(heap,intervals[i][1])
        else:
            heappush(heap,intervals[i][1])
    
        maxRooms=max(maxRooms,len(heap))
    return maxRooms


# youtube reference : 
# https://www.youtube.com/watch?v=NKf1OJhEZj0&t=1535s

intervals=[[1,3],[5,6]]
print(minRooms(intervals))