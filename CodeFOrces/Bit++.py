
n=int(input())
cnt=0
for x in range(n):
    p=input()
    if p[1]=='+':
        cnt+=1
    else:
        cnt-=1
print(cnt)