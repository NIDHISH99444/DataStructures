def checkPallindrome(palString):
    # str=palString
    # if str==str[::-1]:
    #     return True
    # else:
    #     return False
    return palString==palString[::-1]

def solve(palString,i,j,t):
    if i>=j:
        return 0
    if checkPallindrome(palString[i:j+1])==True:
        return 0
    if t[i][j]!=-1:
        return t[i][j]
    ans=100
    for k in range(i,j):
        if t[i][k] != -1:
            left = t[i][k]
        else:
            left = solve(palString, i, k, t)
        if t[k + 1][j] != -1:
            right = t[k+1][j]
        else:
            right = solve(palString, k + 1, j, t)
        temp = left + right + 1
        #temp=solve(palString,i,k,t)+solve(palString,k+1,j,t)+1
        ans=min(ans,temp)
    t[i][j]=ans
    return ans

PalliString="dVGAaVO25EmT6W3zSTEA0k12i64Kkmmli09Kb4fArlF4Gc2PknrlkevhROxUg"

t=[[-1 for i in range(len(PalliString))]for j in range(len(PalliString))]

print(solve(PalliString,0,len(PalliString)-1,t))
print(t)
