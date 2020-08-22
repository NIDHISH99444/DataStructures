
# Given a NxM matrix containing Uppercase English Alphabets only. Your task is to tell if there is a path in the given matrix which makes the sentence “CODINGNINJA” .
# There is a path from any cell to all its neighbouring cells. A neighbour may share an edge or a corner.
# Input Format :
# Line 1 : Two space separated integers N  and M, where N is number of rows and M is number of columns in the matrix.
# Next N lines : N rows of the matrix. First line of these N line will contain 0th row of matrix, second line will contain 1st row and so on
# Assume input to be 0-indexed based
# Output Format :
# Return 1 if there is a path which makes the sentence “CODINGNINJA” else return 0.
# Constraints :
# 1 <= N <= 100
# 1 <= M <= 100
# Sample Input :
# 2 11
# CXDXNXNXNXA
# XOXIXGXIXJX
# Sample Output :
# 1




def codingNinjas(matrix,i,j,word,count):
    if count==len(word):
        return True
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]!=word[count]:
        return False
    temp=matrix[i][j]
    matrix[i][j]='#'
    found=codingNinjas(matrix,i-1   , j-1  ,word,count+1)  \
    or codingNinjas(matrix, i - 1, j    , word, count + 1) \
    or codingNinjas(matrix, i - 1, j + 1, word, count + 1) \
    or codingNinjas(matrix, i    , j + 1, word, count + 1) \
    or codingNinjas(matrix, i + 1, j + 1, word, count + 1) \
    or codingNinjas(matrix, i + 1, j    , word, count + 1) \
    or codingNinjas(matrix, i + 1, j - 1, word, count + 1) \
    or codingNinjas(matrix, i    , j - 1, word, count + 1)
    matrix[i][j]=temp
    return found







matrix=[]
n,m=list(map(int,input().split()))
for i in range(n):
    m=input()
    lst=[char for char in m]
    matrix.append(lst)
word="CODINGNINJA"
#matrix=[['C', 'X', 'D', 'X', 'N', 'X', 'N', 'X', 'N', 'X', 'A'], ['X', 'O', 'X', 'I', 'X', 'G', 'X', 'I', 'X', 'J', 'X']]

def checkString(word,matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==word[0]:
                if codingNinjas(matrix,i,j,word,0):
                    return 1
    return 0


print(checkString(word,matrix))
