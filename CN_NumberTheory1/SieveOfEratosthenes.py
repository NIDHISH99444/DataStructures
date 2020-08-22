#find the total no of prime numbers in the range(1,n)


import math
def countPrime(n):
    arr=[True]*(n+1)
    arr[0]=False
    arr[1]=False
    range1=int(1+math.sqrt(n))
    for i in range(2,range1):
        if i==False:
            continue

        for j in range(i*i,n+1,i):
            arr[j]=False
    count=0
    print(arr)
    for i in range(len(arr)):
        if arr[i]==True:
            count+=1
    return count




print(countPrime(25))