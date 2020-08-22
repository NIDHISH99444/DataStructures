

def area(A):
    matrix=[[0 for i in range(len(A[0]))]for j in range(len(A))]
    for i in range(len(A)):
        matrix[i][0]=A[i][0]
    for i in range(len(A[0])):
        matrix[0][i]=A[0][i]
    for i in range(1,len(A)):
        for j in range(1,len(A[0])):
            if A[i][j]!=0:
                matrix[i][j]=min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1])+1
    maxVal=-1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            maxVal=max(maxVal,matrix[i][j])
    return maxVal*maxVal

A = [

        [0, 1, 1, 0, 1],

        [1, 1, 0, 1, 0],

        [0, 1, 1, 1, 0],

        [1, 1, 1, 1, 0],

        [1, 1, 1, 1, 1],

        [0, 0, 0, 0, 0]
     ]

print(area(A))