intervals = [[7,10],[2,4]]

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x : x[0])
    res=[]
    res.append(intervals[0])
    for i in range(1,len(intervals)):
        if intervals[i][0]>=res[-1][1]:
            res.append(intervals[i])
        else:
            return False
    return True
    




print(canAttendMeetings(intervals))