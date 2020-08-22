

def lcs(a,b,n,m):

    matrix=[[0 for i in range(m+1)]for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                 matrix[i][j]=1+matrix[i-1][j-1]
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
    return (matrix[n][m])


A = "abbc"
B = "bbade"

n=len(A)
m=len(B)
print(lcs(A,B,n,m))