#codeshef problem
#https://www.codechef.com/problems/CHEFRES

def chefProblem(interval,k):
    interval=sorted(interval,key=lambda x:x[0])
    start=0
    ans=-1
    end=len(interval)-1
    while start<=end:
        mid=(start+end)//2
        if interval[mid][0]>=k:
            ans=mid
            end=mid-1
        else :
            start=mid+1
    print(ans)
    if ans==-1:
        return -1
    if ans==0:
        return interval[0][0]-k
    if interval[ans][0]==k:
        return 0
    elif interval[ans-1][1]>k:
        return 0
    else:
        return interval[ans][0]-k




print(chefProblem([(4,5),(5,7),(9,10),(2,3),(20,30)],1))