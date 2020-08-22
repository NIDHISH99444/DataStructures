#https://www.codechef.com/ZCOPRAC/problems/ZCO15002
#using 2 pointer approach

def solution(arr,k):
    arr.sort()
    i=0
    j=i+1
    cnt=0
    while i<len(arr)-1 and j<len(arr):
        if arr[j]-arr[i]>=k:
            cnt+=len(arr)-j
            i+=1
            if i==j:
                j+=1
        else:
            j+=1
    return cnt


#print pairs whose difference is >=k
# n,m=map(int,input().split())
# lst=list(map(int,input().split()))
# print(solution(lst,m))
#print(solution([1,7,3,11,13,17],4))
print(solution([3,1,3],1))