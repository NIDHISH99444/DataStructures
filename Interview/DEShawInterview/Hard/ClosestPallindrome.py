import  sys
def checkAll9(n):
    for ele in n:
        if int(ele)!=9:
            return False
    return True

def check(fh,carry,size):
    fh=list(fh)
    if carry==-1:
        i=size-1
        while i>=0 and fh[i]==0:
            fh[i]='9'
            i-=1
        if i>=0:
            fh[i]=str(int(fh[i])-1)
        return ("".join(fh))
    if carry==1:
        i=size-1
        while i>=0 and carry==1:
            digit=int(fh[i])
            fh[i]=str((int(fh[i])+1)%10)
            carry=(carry+digit)//10
            i-=1
        return ("".join(fh))
def closestPallindrome(string):

    if len(string)==1:
        return int(string)-1
    # if checkAll9(string):
    #     return "1"+"0"*(len(string)-1)+"1"
    if len(string) != 1 and string[:-1] == '1' + '0' * (len(string) - 2) and (string[-1] == '0' or string[-1] == '1'):
        return '9' * (len(string) - 1)
    elif string == '9' * len(string) and len(string) != 1:
        return '1' + '0' * (len(string) - 1) + '1'
    upper_reflection=0
    lower_reflection=0
    reflection=0
    middle = int(len(string) // 2)
    if len(string)%2!=0:

        fh=string[0:middle]
        mdl=string[middle]

        sh=fh[::-1]
        reflection=fh+mdl+sh
        if int(mdl) == 9:
            fhu=check(fh, 1, len(fh))
            print(fhu)
            shu=fhu[::-1]
            upper_reflection = fhu + "0" + shu
        else:
            upper_reflection = fh + str(int(mdl)+1) + sh
        if int(mdl) == 0:
            fhl=check(fh, -1, len(fh))
            print(fhl)
            shl=fhl[::-1]
            lower_reflection=fhl+"9"+shl
        else:
            lower_reflection = fh + str(int(mdl)-1) + sh
        print(reflection,lower_reflection,upper_reflection)
    elif len(string)%2==0:
        fh = string[0:middle-1]+string[middle-1]
        fhLow=string[0:middle - 1] + str(int(string[middle - 1]) - 1)
        fhupp=string[0:middle - 1] + str(int(string[middle - 1]) + 1)
        sh,shlow,shupp = fh[::-1],fhLow[::-1],fhupp[::-1]

        reflection=fh+sh
        lower_reflection=fhLow+shlow
        upper_reflection=fhupp+shupp
        print(reflection,lower_reflection,upper_reflection)
    minDiff=sys.maxsize
    minValue=0
    if abs(int(string)-int(reflection))!=0:
        minDiff=min(abs(int(string)-int(reflection)),minDiff)
        minValue=reflection

    if abs(int(string)-int(upper_reflection))<=minDiff:
        minDiff=abs(int(string)-int(upper_reflection),minDiff)
        minValue=upper_reflection
    if abs(int(string) - int(lower_reflection)) <minDiff:
        minDiff = abs(int(string) - int(lower_reflection), minDiff)
        minValue = lower_reflection
    return minValue




print(closestPallindrome("1837722381"))