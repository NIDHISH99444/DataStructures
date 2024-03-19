board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

def dfs(board,i,j,word,wordLen,cnt,visited):
    if cnt==wordLen:
        return True
    visited[i][j]=True
    rows=[-1,0,1,0]
    cols=[0,1,0,-1]
    for k in range(len(rows)):
        nextRow=i+rows[k]
        nextCol=j+cols[k]
        if nextRow >=0 and nextRow<len(board) and nextCol>=0 and nextCol<len(board[0]) and visited[nextRow][nextCol]==False and word[cnt]==board[nextRow][nextCol]:
            if dfs(board,nextRow,nextCol,word,wordLen,cnt+1,visited) :
                return True 
    visited[i][j] = False
    return False


def exist( board, word):
    wordLen=len(word)
    cnt=1
    visited=[[0 for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==word[0]:
               if dfs(board,i,j,word,wordLen,cnt,visited) ==True:
                   return True
    return False



print(exist( board, word))
