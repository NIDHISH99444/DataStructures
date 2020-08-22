def check(A):
    inc=max(A[0][0],A[1][0])
    
    exc=0
    for i in range(1,len(A[0])):
        old=inc
        inc=max(exc+max(A[0][i],A[1][i]),inc)
        exc=inc
    return inc


A = [[1, 2, 3, 4],
     [2, 3, 4, 5]]

print(check(A))
