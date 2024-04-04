
s = "bb"

def checkPallindrome(string,i,j):
    
    while i>=0 and j<len(string) and string[i]==string[j]:
        i-=1
        j+=1
         
    return string[i+1:j]
   


def longestPalindrome(string1):
    res,maxLen="",0
    for i in range(len(string1)):
        l,r=i,i
        derString=checkPallindrome(string1,l,r)
        l,r=i,i+1
        derString1=checkPallindrome(string1,l,r)
        print(derString,derString1)

        if maxLen<len(derString):
            maxLen=len(derString)
            res=derString
        if maxLen<len(derString1):
            maxLen=len(derString1)
            res=derString1
        
    return res

        
    






print(longestPalindrome(s))

    



