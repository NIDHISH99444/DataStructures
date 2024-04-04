
s = "aaa"

def checkPallindrome(string,i,j):
    cnt=0
    while i>=0 and j<len(string) and string[i]==string[j]:
        i-=1
        j+=1
        cnt+=1
    return cnt
    
   


def longestPalindrome(string1):
    cnt=0
    for i in range(len(string1)):
        l,r=i,i
        cnt1=checkPallindrome(string1,l,r)
        l,r=i,i+1
        cnt2=checkPallindrome(string1,l,r)
    
        cnt+=cnt1+cnt2
        
    return cnt

        
    






print(longestPalindrome(s))

    



