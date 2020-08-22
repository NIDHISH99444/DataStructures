from collections import Counter
def findAllAnagrmaString(s,p):
    j = len(p)
    res=[]

    arr1=Counter(p)

    arr2=Counter(s[:j])

    if arr1==arr2:
        res.append(0)


    for i in range(j,len(s)):
        arr2[s[i-j]]-=1
        if arr2[s[i-j]]==0:
            del arr2[s[i-j]]
        arr2[s[i]]+=1
        if arr1==arr2:
            res.append(i-j+1)
    return res



s= "cbaebabac"
p= "abc"
print(findAllAnagrmaString(s,p))