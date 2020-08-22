
def checkExpr(exp,i,j,isTrue):
    if i>j:
        return 0
    if i==j:
        if isTrue==True:
            return exp[i]=='T'
        else:
            return exp[i]=='F'
    ans=0
    for k in range(i+1,j,2):
        lt=checkExpr(exp,i,k-1,True)
        lf=checkExpr(exp,i,k-1,False)
        rt=checkExpr(exp,k+1,j,True)
        rf=checkExpr(exp,k+1,j,False)
        if exp[k]=='&':
            if isTrue==True:
                ans+=lt*rt
            else:
                ans+=lt*rf+lf*rt+lf*rf
        elif exp[k]=='|':
            if isTrue==True:
                ans+=lt*rf+lf*rt+lt*rt
            else:
                ans += lf * rf
        elif exp[k]=='^':
            if isTrue==True:
                ans += lt * rf + lf * rt
            else:
                ans += lt * rt + lf * rf

    return ans
exp="T^F&T"
isTrue=True
print(checkExpr(exp,0,len(exp)-1,isTrue))