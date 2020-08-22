from collections import Counter

def solve(arr):
    i,j,best,count=0,0,0,0
    last=Counter()
    for j in range(len(arr)):
        if arr[j] not in last:
            count+=1
        last[arr[j]]+=1
        while count>2:
            last[arr[i]]-=1
            if last[arr[i]]==0:
                count-=1
            i+=1
        best=max(best,j-i+1)
    return best

print(solve("ccaabbb"))


