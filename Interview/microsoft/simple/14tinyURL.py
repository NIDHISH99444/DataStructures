import math
def tinyUrl(n):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    res=""
    while n!=0:
        val=(n//62)
        res+=map[(n-(val*62))]
        n=val
    return res[::-1]






n=12345

print(tinyUrl(n))