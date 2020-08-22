

def checkList(list):
    res=[int(i) for i in list if i!='.']
    if len(res)==len(set(res)):
        return True
    else:
        return False

def boxCheck(arr):

    for i in (0,3,6):
        for j in (0,3,6):
            matrix=[arr[x][y] for x in range(i,i+3) for y in range(j,j+3) ]
            if not checkList(matrix):
                return False
        return True
def colCheck(arr):
    for col in zip(*arr):
        if not checkList(col):
            return False
    return True

def rowCheck(arr):
    for row in arr:
        if not checkList(row):
            return False
    return True

def checkValid(arr):
    if rowCheck(arr) and colCheck(arr) and boxCheck(arr):
        return True
    return False

arr=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(colCheck(arr))
