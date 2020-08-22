# Let A[0 ... n-1] be an array of n distinct positive integers. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A (where i and j are indexes of A). Given an integer array A, your task is to find the number of inversions in A.
# Input format :
# Line 1 : n, array size
# Line 2 : Array elements (separated by space).
# Output format :
# Count of inversions
# Constraints :
# 1 <= n <= 10^5
# 1 <= A[i] <= 10^9
# Sample Input 1 :
# 3
# 3 2 1
# Sample Output 1 :
# 3
# Sample Input 2 :
# 5
# 2 5 1 3 4
# Sample Output 1 :
# 4


def merge(arr,left,mid,right):
    i=left
    j=mid
    k=0
    count=0
    temp=[0]*(right-left+1)
    while i<mid and j<=right:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            i+=1
            k+=1
        else:
            temp[k]=arr[j]
            j+=1
            k+=1
            count+=(mid-i)
    while i <mid :
        temp[k]=arr[i]
        k+=1
        i+=1
    while j<=right:
        temp[k]=arr[j]
        k+=1
        j+=1
    p=0
    for s in range(left,right+1):
        arr[s]=temp[p]
        p+=1
    return count

def mergeSort(arr,left,right):
    count=0
    if right>left:
        mid=(left+right)//2
        countLeft=mergeSort(arr,left,mid)
        countRight=mergeSort(arr,mid+1,right)
        myCount=merge(arr,left,mid+1,right)
        return myCount+countLeft+countRight
    return count
def inversionCount(arr):
    print(mergeSort(arr,0,len(arr)-1))

inversionCount([5,4,2,3,1])