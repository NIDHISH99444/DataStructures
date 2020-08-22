from sys import maxsize
def rodCutting(length,price,W):
    matrix=[[maxsize for i in range(W+1)]for j in range(len(length)+1)]
    for i in range(len(length)+1):
        matrix[i][0]=0

    for i in range(1,len(length)+1):
        for j in range(1,W+1):
            if length[i-1]<=j:
                matrix[i][j]=min(matrix[i-1][j],price[i-1]+matrix[i][j-length[i-1]])
            else:
                matrix[i][j]=matrix[i-1][j]
    return (matrix[-1][-1])
A=   [ 2, 4, 6]
B=[2,1,3]
C=[2,5,3]

res=0
for i in range(1,len(A)):

    W=A[i]
    length=B[1:]
    price=C[1:]
    res+=(rodCutting(length,price,W))
print(res)