def isInter(a, b, c, cache):
    if len(a)==0 and len(b)==0 and len(c)==0:
        return True
    key=(len(a),len(b),len(c))
    if key in cache:
        return cache[key]
    r=False
    if len(a)>0 and len(c)>0 and a[0]==c[0]:
        r |= isInter(a[1:],b,c[1:],cache)
    if len(b) > 0 and len(c) > 0 and b[0] == c[0]:
        r |= isInter(a, b[1:], c[1:], cache)

    cache[key]=r
    return r


def isInterleave( A, B, C):
    if (isInter(A, B, C, {})):
        return 1
    return 0


A = "ac"
B = "adbc"
C = "adbacc"
print(isInterleave(A,B,C))