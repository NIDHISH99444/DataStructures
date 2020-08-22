

def cnt(tmp):
    x=1
    while tmp>1:
        tmp//=2
        x*=2
    return x

n=10
x=cnt(n)
print(x)
x=2*n-1
print(x)