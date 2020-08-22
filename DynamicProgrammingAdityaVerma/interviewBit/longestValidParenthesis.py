def longestValidParentheses( s):
    """
    :type s: str
    :rtype: int
    """
    stack = [-1]
    maxVal = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack)==0:
                stack.append(i)
            else:
                maxVal=max(maxVal,i-stack[-1])



    return maxVal


print(longestValidParentheses(")()())"))