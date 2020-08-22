#https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/
def MAxSumPath2Array(arr1,arr2):
    sum1,sum2,totalSum=0,0,0
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if i<len(arr1) and arr1[i]<arr2[j]:
            sum1+=arr1[i]
            i+=1
        elif j<len(arr2) and arr1[i]>arr2[j]:
            sum2+=arr2[j]
            j+=1
        else:
            totalSum+=max(sum1,sum2)
            totalSum+=arr1[i]
            i+=1
            j+=1
            sum1,sum2=0,0
    while i<len(arr1):
        sum1+=arr1[i]
        i+=1
    if j<len(arr2):
        sum2+=arr2[j]
        j+=1
    totalSum+=max(sum1,sum2)
    return totalSum



ar1= [10,12]
ar2= [ 5, 7, 8]
print(MAxSumPath2Array(ar1,ar2))