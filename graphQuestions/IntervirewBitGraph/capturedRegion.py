def addBoundary(matrix,i,j):

    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]=='X' or matrix[i][j]=='B' :
        return
    matrix[i][j]='B'
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for s in range(len(dx)):
        addBoundary(matrix,i+dx[s],j+dy[s])
def captured(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i in (0,len(matrix)-1) or j in (0,len(matrix[0])-1)) and matrix[i][j]=='O':
                addBoundary(matrix,i,j)
    print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='O':
                matrix[i][j]='X'
            elif matrix[i][j]=='B':
                matrix[i][j]='O'
    print(matrix)


matrix = [
     ['X', 'O','X', 'X'],
     ['X','O', 'O', 'X'],
     ['X', 'X', 'O', 'X'],
     ['X', 'X', 'X', 'X']
     ]
captured(matrix)