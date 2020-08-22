def domino(a,b):
    sum=0
    sum+=a*(b//2)
    if b%2==1:
        sum+=a//2
    return sum


a,b=map(int,input().split())
print(domino(a,b))