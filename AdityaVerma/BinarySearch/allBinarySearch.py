def firstOccurance(arr,ele):
    res=-1
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==ele:
            res=mid
            end=mid-1
        elif arr[mid]>ele:
            end=mid-1
        else:
            start=mid+1
    return res

def lastOccurance(arr,ele):
    res=-1
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==ele:
            res=mid
            start=mid+1
        elif arr[mid]>ele:
            end=mid-1
        else:
            start=mid+1
    return res


def firstLastOccurance(arr,ele):
    firstOccur=firstOccurance(arr,ele)
    lastOccur=lastOccurance(arr,ele)
    return [firstOccur,lastOccur]

arr=[5, 7, 7, 8, 8, 10]
target=6
#print(firstLastOccurance(arr,target))

def noOftimesArrayRotated(arr):

    start=0
    end=len(arr)-1
    if arr[start] < arr[end]:
        return start
    while start<=end:

        mid=start+(end-start)//2
        prev=(mid+len(arr)-1)%(len(arr))
        next=(mid+1)%len(arr)
        if arr[mid]<=arr[prev] and arr[mid]<=arr[next]:
            return mid
        elif arr[mid]>=arr[start]:
            start=mid+1
        elif arr[mid]<=arr[end]:
            end=mid-1


arr=[3,0]
print("no of times array rotated ")
print(noOftimesArrayRotated(arr))

def findElementDecreasing(arr,ele,start,end):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            start=mid+1
        else:
            end=mid-1
    return -1

def findElementIncreasing(arr,ele,start,end):

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            end=mid-1
        else:
            start=mid+1
    return -1




###Find element in rotated sorted Array

def findElementRotatedSortedArray(arr,key):
    index=noOftimesArrayRotated(arr)
    print("index",index)
    resL=findElementIncreasing(arr,key,0,index)
    resR=findElementIncreasing(arr,key,index,len(arr)-1)
    if resL==-1:
        return resR
    else:
        return resL

arr=[3,1]
print(findElementRotatedSortedArray(arr,0))
###Search is nearly sorted array

def findFloor(arr,ele):
    start=0
    res=-1
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==ele:
            return arr[mid]
        elif arr[mid]<ele:
            res=arr[mid]
            start=mid+1
        else:
            end=mid-1
    return res

arr= [1, 2, 8, 10, 10, 12, 19]
x = 2
#print(findFloor(arr,x))

def findCeil(arr,ele):
    start=0
    res=-1
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==ele:
            return arr[mid]
        elif arr[mid]<ele:

            start=mid+1
        else:
            res = arr[mid]
            end=mid-1
    return res

arr= [1, 2, 8, 10, 10, 12, 19]
x = 7
#print(findCeil(arr,x))

def findNextAlphabet(arr,alpha):
    start=0
    finalAlpha=""
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==alpha:
            start=mid+1
        elif arr[mid]>alpha:
            finalAlpha=arr[mid]
            end=mid-1
        else:
            start=mid+1
    if (mid==len(arr)-1):
        return arr[0]

    return finalAlpha

arr=["b","c","f","h"]
#print(findNextAlphabet(arr,"d"))

def minDifferenceElementSortedArray(arr,key):
    # ceil=findCeil(arr,key)
    # flor=findFloor(arr,key)
    # return  min(abs(ceil-key),abs(flor-key))
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==key:
            return [arr[mid],arr[mid]]
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return [arr[low],arr[high]]
arr=[1,3,6,12,15]
key=8
low,high=minDifferenceElementSortedArray(arr,key)
#print(low,high)
#print(min(abs(high-key),abs(low-key)))


def peakElementIndex(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if mid > 0 and mid< len(arr)-1 :
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1]:
                start=mid+1
            else :
                end=mid-1
        elif mid==0:
            if arr[0]>arr[1]:
                return 0
            else:
                return 1
        elif mid==len(arr)-1:
            if arr[mid]>arr[mid-1]:
                return mid
            else:
                return mid-1


arr=[1,2,1,3,5,6,4]
#print(peakElementIndex(arr))



def findingElementBitonicArray(arr,key):
    index=peakElementIndex(arr)
    resI=findElementIncreasing(arr,key,0,index)
    resD=findElementDecreasing(arr,key,index,len(arr)-1)
    if resI==-1:
        return resD
    else:
        return resI


arr=[-3, 8,9, 20, 17, 5, 1]
key=5
#print(findingElementBitonicArray(arr,key))