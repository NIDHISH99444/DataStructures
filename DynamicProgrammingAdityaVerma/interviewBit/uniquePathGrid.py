

def area(A):
    matrix=[[0 for i in range(len(A[0]))]for j in range(len(A))]
    for i in range(len(A)):
        if A[i][0]==0:
            matrix[i][0]=1
        else:
            break
    for i in range(len(A[0])):
        if A[0][i]==0:
            matrix[0][i]=1
        else:
            break
    for i in range(1,len(A)):
        for j in range(1,len(A[0])):
            if A[i][j]!=1:
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
    return matrix[-1][-1]

A=[
  [1,0]
]

print(area(A))