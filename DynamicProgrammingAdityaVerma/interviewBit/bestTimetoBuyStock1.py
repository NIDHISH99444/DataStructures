def nextSmallestLeftIndex( arr):
    res = []
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            res.append(-1)
        elif arr[i] > stack[-1][0]:
            res.append(stack[-1][1])
        elif len(stack) != 0 and arr[i] <= stack[-1][0]:
            while len(stack) != 0 and arr[i] <= stack[-1][0]:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append([arr[i], i])
    print(res)
    return (res)


def nextSmallestRightIndex( arr):
    res = []
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        if len(stack) == 0:
            res.append(-1)
        elif arr[i] > stack[-1][0]:
            res.append(stack[-1][1])
        elif len(stack) != 0 and arr[i] <= stack[-1][0]:
            while len(stack) != 0 and arr[i] <= stack[-1][0]:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append([arr[i], i])
    print(res)
    return (res[::-1])


def largestRectangleArea( arr):
    """
    :type heights: List[int]
    :rtype: int
    """
    arr.append(0)
    leftWindow = nextSmallestLeftIndex(arr)
    rightWindow = nextSmallestRightIndex(arr)
    newWindow = [0] * (len(leftWindow) - 1)
    for i in range(len(leftWindow) - 1):
        newWindow[i] = rightWindow[i] - leftWindow[i] - 1
    print(newWindow)
    maxRes = 0
    for i in range(len(arr) - 1):
        maxRes = max(maxRes, arr[i] * newWindow[i])
    return (maxRes)

area=[2,1,5,6,2,3]
print(largestRectangleArea(area))