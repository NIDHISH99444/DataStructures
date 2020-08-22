
def area(A):
    matrix=[[0 for i in range(len(A[0]))]for j in range(len(A))]
    matrix[0][0]=A[0][0]
    for i in range(1,len(A)):
        matrix[i][0]=matrix[i-1][0]+A[i][0]
    for i in range(1,len(A[0])):
        matrix[0][i]=matrix[0][i-1]+A[0][i]
    for i in range(1,len(A)):
        for j in range(1,len(A[0])):
            if matrix[i-1][j]<matrix[i][j-1]:
                matrix[i][j]=matrix[i-1][j]+A[i][j]
            else:
                matrix[i][j]=matrix[i][j-1]+A[i][j]
    return (matrix[-1][-1])

A=[  [1, 3, 2],
        [4, 3, 1],
        [5, 6, 1]
     ]

print(area(A))