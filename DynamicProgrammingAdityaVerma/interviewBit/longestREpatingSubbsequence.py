

def lcs(a,b):
    matrix = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1] and i!=j :
                matrix[i][j] = matrix[i - 1][j - 1]+1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return (matrix[-1][-1])>=2


A = "abba"
B=A


print(lcs(A,B))