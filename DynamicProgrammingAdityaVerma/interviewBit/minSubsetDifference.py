from sys import  maxsize
def minSubDiff(arr,l):
    matrix=[[False for i in range(l+1)]for j in range(len(arr)+1)]
    for i in range(len(arr)+1):
        matrix[i][0]=True
    for i in range(1,len(arr)+1):
        for j in range(1,l+1):
            if arr[i-1]<=j:
                matrix[i][j]=matrix[i-1][j] or matrix[i-1][j-arr[i-1]]
            else:
                matrix[i][j]=matrix[i-1][j]
    ms=(matrix[-1])
    resArray=[]
    for i in range(len(ms)):
        if ms[i]==True:
            resArray.append(i)
    print(resArray)
    minDiff=maxsize
    for i in range(len(resArray)//2):
        minDiff=min(l-2*resArray[i],minDiff)
    print(minDiff)
arr=a =  [ 7, 2, 94, 49, 30, 24, 85, 55, 57, 41 ]
#arr=[1,2,7]
len1=sum(arr)
print(len1)


minSubDiff(arr,len1)