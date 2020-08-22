import sys
def largestSum(arr):
    meh=-sys.maxsize
    msf=0
    for i in range(len(arr)):
        msf+=arr[i]
        meh=max(meh,msf)
        if msf<0:
            msf=0
    return meh

print(largestSum([-2,-1,-3]))