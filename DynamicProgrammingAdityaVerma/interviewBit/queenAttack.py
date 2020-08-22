from collections import  defaultdict
def queenAttack( A):
    n, m = len(A), len(A[0])
    res = [[0] * m for _ in range(n)]

    hasTop = [0] * m
    hasDiag = defaultdict(int)
    hasRdiag = defaultdict(int)
    for i in range(n):
        hasLeft = 0
        for j in range(m):
            res[i][j] += hasLeft + hasTop[j] + hasDiag[j - i] + hasRdiag[j + i]
            if A[i][j] == '1':
                hasLeft = 1
                hasTop[j] = 1
                hasDiag[j - i] = 1
                hasRdiag[j + i] = 1

    hasBottom = [0] * m
    hasDiag = defaultdict(int)
    hasRdiag = defaultdict(int)
    for i in range(n - 1, -1, -1):
        hasRight = 0
        for j in range(m - 1, -1, -1):
            res[i][j] += hasRight + hasBottom[j] + hasDiag[j - i] + hasRdiag[j + i]
            if A[i][j] == '1':
                hasRight = 1
                hasBottom[j] = 1
                hasDiag[j - i] = 1
                hasRdiag[j + i] = 1

    return res

matrix=[
['0','1' ,'0'],
['1', '0','0'],
['0' ,'0' ,'1']
]
print(queenAttack(matrix))

