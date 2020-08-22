def nextRound(ll,k):
    cnt=0
    for i in range(len(ll)):
        if ll[i]>=ll[k-1] and ll[i]>0:
            cnt+=1
    return cnt



n,k=map(int,input().split())
ll=list(map(int,input().split()))
print(nextRound(ll,k))
