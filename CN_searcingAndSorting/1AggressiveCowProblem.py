# Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).
# His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
# Input
# t – the number of test cases, then t test cases follows.
# * Line 1: Two space-separated integers: N and C
# * Lines 2..N+1: Line i+1 contains an integer stall location, xi
# Output
# For each test case output one integer: the largest minimum distance.
# Sample Input :
# 1
# 5 3
# 1
# 2
# 8
# 4
# 9
# Sample Output:
# 3
# Output details:
# FJ can put his 3 cows in the stalls at positions 1, 4 and 8,
# resulting in a minimum distance of 3.

def check(position,distance,cows):
    count=1
    last_index=position[0]
    for i in range(1,len(position)):
        if position[i]-distance>=last_index:
            last_index=position[i]
            count+=1
        if count==cows:
            return True
    return False
def aggressiveCowProblem(position,cows):
    position.sort()
    start=0
    end=position[len(position)-1]-position[0]
    ans=-1
    while start<=end:
        mid =start+(end-start)//2
        if check(position,mid,cows):
            ans=mid
            start=mid+1
        else:
            end=mid-1
    return ans
#
n=int(input())
res=[]
ipt,cows=map(int,input().split())
print(ipt,cows)
for i in range(ipt):
    res.append(int(input()))
print(aggressiveCowProblem(res,cows))

#print(aggressiveCowProblem([100000000,500000000,900000000,1],2))
#
# 1
# 20 3
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
#
# 1
# 4 2
# 100000000
# 500000000
# 900000000
# 1