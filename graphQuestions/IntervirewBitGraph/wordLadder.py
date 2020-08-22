def wordLadder(beginWord,endWord,wordList):
    if endWord not in wordList:
        return -1
    wordList=set(wordList)
    step=1
    print(wordList)
    q=[]
    q.append((beginWord,step))
    while q:
        newWord,step=q.pop(0)
        if newWord==endWord:
            return step
        for i in range(len(newWord)):
            for j in "lothdgcd":
                nextWord=newWord[:i]+j+newWord[i+1:]
                if nextWord in wordList:
                    wordList.remove(nextWord)
                    q.append((nextWord,step+1))
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","hot","dot","dog","lot","log","cog"]
A ="ymain"
B = "oecij"
C = [ "ymann", "yycrj", "oecij", "ymcnj", "yzcrj", "yycij", "xecij", "yecij", "ymanj", "yzcnj", "ymain" ]

print(wordLadder(A,B,C))
