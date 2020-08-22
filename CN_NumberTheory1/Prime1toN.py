import math
def checkPrime(num):
    count=0
    range1=int(math.sqrt(num)+1)
    for j in range(1,range1):
        if num%j==0 and j*j!=num:
            count+=2
        if j*j==num:
            count+=1
    if count==2:
        return True
    else:
        return False


def countPrime(n):
    count=0
    for i in range(1,n+1):
        if checkPrime(i):
            count+=1
    return count


n=int(input())
print(countPrime(n))