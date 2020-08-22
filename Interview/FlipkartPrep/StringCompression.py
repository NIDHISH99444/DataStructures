def stringcompression(string):
    rptr,wprt=0,0

    while rptr<len(string):
        ch=string[rptr]
        cnt=0
        while rptr<len(string) and ch==string[rptr]:
            cnt+=1
            rptr+=1
        string[wprt]=ch
        wprt+=1
        if cnt>1:
            for ele in str(cnt):
                string[wprt]=ele
                wprt+=1
    return "".join(string[:wprt])
print(stringcompression(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))