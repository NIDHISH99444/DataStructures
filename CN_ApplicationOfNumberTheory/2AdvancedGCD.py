def gcdCalc(a,b):
    if a==0:
        return b
    return gcdCalc(b,a%b)
def gcd(a,b):
    numb=reduce(b)
    return gcdCalc(a,numb)