
from collections import deque

def wordLadder(beginWord,endWord,wordList):
    s=set(wordList)
    q=deque()
    if endWord not in s:
        return 0
    step=1
    q.append((beginWord,step))
    while q :
        nxtWord,step=q.popleft()
        if nxtWord == endWord:
            return step
        for i in range(len(nxtWord)):
             for chr in "htdog":
                 newWord=nxtWord[:i]+chr+nxtWord[i+1:]
                 if newWord in s:
                    s.remove(newWord)
                    q.append((newWord,step+1))
    return step

    #
    # s = set(wordList)
    # if endWord not in wordList:
    #     return 0
    # step = 1
    # q = deque()
    # q.append((beginWord, step))
    #
    # while q:
    #     word, step = q.popleft()
    #     if word == endWord:
    #         return step
    #     for i in range(len(word)):
    #         for char in 'abcdefghijklmnopqrstuvwxyz':
    #             newWord = word[:i] + char + word[i + 1:]
    #             if newWord in s:
    #                 s.remove(newWord)
    #                 q.append((newWord, step + 1))
    # return 0
beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
print(wordLadder(beginWord,endWord,wordList))