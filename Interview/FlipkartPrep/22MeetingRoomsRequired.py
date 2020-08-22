def meetingTiming(start,end):
    start.sort()

    end.sort()

    cnt=1
    i,j=1,0
    maxCnt=0
    while i <len(start) and j<len(end):
        if start[i]<end[j]:
            cnt+=1
            maxCnt=max(maxCnt,cnt)
            i+=1
        else:
            j+=1
            cnt-=1

    return maxCnt





start = [900, 940, 950, 1100, 1500, 1800]
end = [910, 1120, 1130, 1200,1900, 2000]
print(meetingTiming(start,end))