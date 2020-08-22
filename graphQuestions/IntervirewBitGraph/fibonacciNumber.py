def fibsum( A):
    f,s=1,1
    res=[]
    res.append(f)
    res.append(s)
    while True:
        third=f+s
        if third<=A:
            res.append(third)
            f=s
            s=third
        else:
            break
    ans=0
    for i in range(len(res)-1,-1,-1):
        if res[i]<=A:
            A-=res[i]
            ans+=1
    return ans



print(fibsum(10))