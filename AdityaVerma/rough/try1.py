def decodeString(s):

    stack=[]
    res=''
    number=''
    for i in range(len(s)):
        if s[i]!="]":
            stack.append(s[i])
        elif s[i]==']':
            while stack[-1]!='[':
                res+=stack.pop()
            res=res[::-1]
            stack.pop()
            while stack[-1].isdigit():
                number+=stack.pop()
            number=number[::-1]
            number=int(number)
            stack.append(number*res)
    return "".join(stack)

s = "3[a2[cd]]"
# Output: "aaabcbc"
print(decodeString(s))