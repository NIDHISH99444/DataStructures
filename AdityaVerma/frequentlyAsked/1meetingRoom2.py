from heapq import heappush,heappop
def minRooms(intervals):
    intervals.sort(key=lambda x : x[0])
    heap=[]
    maxRooms=0
    for i in range(len(intervals)):
        if not heap : 
            heappush(heap,intervals[i][1])
        elif intervals[i][0]<heap[-1]:
            heappush(heap,intervals[i][1])
        else:
            heappop(heap)
            heappush(heap,intervals[i][1])
        maxRooms=max(maxRooms,len(heap))
    return maxRooms



intervals=[[1,3],[5,6]]
print(minRooms(intervals))