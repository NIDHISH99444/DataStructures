n,m,k=map(int,input().split())
#n,m,k=2,1,1
sum=0
sum1=0
if n%k==0:
    sum=n//k
else:
    sum=(n//k)+1
if m%k==0:
    sum1=m//k
else:
    sum1=(m//k)+1
print(sum*sum1)

