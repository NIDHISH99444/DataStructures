
#1 https://leetcode.com/problems/longest-substring-without-repeating-characters/
#2 https://leetcode.com/problems/substring-with-concatenation-of-all-words/
#3 https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
#4 https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter
#1
def  checkwindowsize(arr):
    last={}
    start=0
    maxlen=0
    cnt=0
    for i in range(len(arr)):

        if arr[i] not in last or last[arr[i]]<start:
            last[arr[i]]=i
            cnt=i-start+1
            maxlen=max(maxlen,cnt)
        else:
            cnt=0
            start=last[arr[i]]+1
            last[arr[i]]=i

    return maxlen
arr="pwwkew"
print(checkwindowsize(arr))

#4

def findAnagram(arr,word):

    n=len(word)
    word=Counter(word)

    newWord=Counter(arr[:n])
    res=[]
    if newWord==word:
        res.append(0)

    for i in range(n,len(arr)):
        newWord[arr[i-n]]-=1
        if newWord[arr[i-n]]==0:
            newWord.pop(arr[i-n])
        newWord[arr[i]]+=1
        if newWord==word:
            res.append(i-n+1)
    return res



        



s= "cbaebabacd"
p= "abc"
print(findAnagram(s,p))