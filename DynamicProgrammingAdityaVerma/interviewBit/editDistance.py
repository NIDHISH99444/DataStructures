

def edit(a,b):


    matrix=[[0 for i in range(len(b)+1)]for j in range(len(a)+1)]
    for i in range(len(a)+1):
        matrix[i][0]=i
    for j in range(len(b)+1):
        matrix[0][j]=j
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                 matrix[i][j]=matrix[i-1][j-1]
            else:
                matrix[i][j]=min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1])+1
    return (matrix[-1][-1])


A = "abbc"
B = "abcbc"


print(edit(A,B))