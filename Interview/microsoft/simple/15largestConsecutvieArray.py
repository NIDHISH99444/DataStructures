from sys import maxsize
def maxCons(arr,maxEndHere,maxSoFar):
    for i in range(len(arr)):
        maxSoFar+=arr[i]
        if maxEndHere<maxSoFar:
            maxEndHere=maxSoFar
        if maxSoFar<0:
            maxSoFar=0
    return maxEndHere


arr=[-2,-3,-1]
maxEndHere=-maxsize
maxSoFar=0
print(maxCons(arr,maxEndHere,maxSoFar))