def dfs(matrix,i,j):
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]=='X' or matrix[i][j]=='D':
        return
    if matrix[i][j]=='O':
        matrix[i][j]='D'
    dfs(matrix, i - 1, j)
    dfs(matrix, i, j + 1)
    dfs(matrix, i + 1, j)
    dfs(matrix, i , j - 1)



def surroundRegion(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='O' and ( i in (0,len(matrix)-1) or j in (0,len(matrix[0])-1)) :
                dfs(matrix,i,j)


    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='D':
                matrix[i][j]='O'
            elif  matrix[i][j]=='O':
                matrix[i][j]='X'

    return matrix

matrix=[["O","O"],["O","O"]]
#matrix=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#matrix=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(surroundRegion(matrix) )