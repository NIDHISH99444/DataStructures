def paranthesis(arr):
    stack=[]
    for i in range(len(arr)):
        if len(stack)==0 and (arr[i]=='}' or arr[i]==']' or arr[i]==')'):
            return False
        elif arr[i]=='{' or arr[i]=='[' or arr[i]=='(':
            stack.append(arr[i])
        elif arr[i]==']' or stack[-1]=='[':
            stack.pop()
        elif arr[i]==')' or stack[-1]=='(':
            stack.pop()
        elif arr[i]=='}' or stack[-1]=='{':
            stack.pop()
    return len(stack)==0





if paranthesis("{([]"):
    print("Balanced")
else:
    print("not")

