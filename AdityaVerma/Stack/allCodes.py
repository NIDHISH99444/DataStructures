def nextGreatestRight(arr):
    res=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            res.append(-1)
        elif arr[i]<stack[-1]:
            res.append(stack[-1])
        elif len(stack)!=0 and arr[i]>=stack[-1]:
            while len(stack)!=0 and arr[i]>=stack[-1]:
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(arr[i])
    print(res[::-1])



arr=[1,3,2,4]
#nextGreatestRight(arr)

def nextGreatestLeft(arr):
    res=[]
    stack=[]
    for i in range(len(arr)):
        if len(stack)==0:
            res.append(-1)
        elif arr[i]<stack[-1]:
            res.append(stack[-1])
        elif len(stack)!=0 and arr[i]>=stack[-1]:
            while len(stack)!=0 and arr[i]>=stack[-1]:
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(arr[i])
    print(res)

#arr=[1,3,2,4]
#nextGreatestLeft(arr)

def nextSmallestRight(arr):
    res=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            res.append(-1)
        elif arr[i]>stack[-1]:
            res.append(stack[-1])
        elif len(stack)!=0 and arr[i]<=stack[-1]:
            while len(stack)!=0 and arr[i]<=stack[-1]:
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(arr[i])
    return (res[::-1])


# arr=[1,3,2,4]
# nextSmallestRight(arr)

def nextSmallestLeft(arr):
    res=[]
    stack=[]
    for i in range(len(arr)):
        if len(stack)==0:
            res.append(-1)
        elif arr[i]>stack[-1]:
            res.append(stack[-1])
        elif len(stack)!=0 and arr[i]<=stack[-1]:
            while len(stack)!=0 and arr[i]<=stack[-1]:
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(arr[i])
    return (res)


arr=[1,3,2,4]
#nextSmallestLeft(arr)

def StockSpan(arr):
    #checking the nextGreatestLeft
    res=[]
    stack=[]
    for i in range(len(arr)):
        if len(stack)==0:
            res.append(-1)
        elif arr[i]<stack[-1][0]:
            res.append(stack[-1][1])
        elif len(stack)!=0 and arr[i]>=stack[-1][0]:
            while len(stack)!=0 and arr[i]>=stack[-1][0]:
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append([arr[i],i])
    newArray=[0]*len(arr)
    print(res)
    for i in range(len(newArray)):
        newArray[i]=i-res[i]
    print(newArray)



arr=[100, 80, 60, 70, 60, 75, 85]
#arr=[10, 4, 5, 90, 120, 80 ]
#StockSpan(arr)

def nextSmallestLeftIndex(arr):
    res=[]
    stack=[]
    for i in range(len(arr)):
        if len(stack)==0:
            res.append(-1)
        elif arr[i]>stack[-1][0]:
            res.append(stack[-1][1])
        elif len(stack)!=0 and arr[i]<=stack[-1][0]:
            while len(stack)!=0 and arr[i]<=stack[-1][0]:
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append([arr[i],i])
    return (res)

def nextSmallestRightIndex(arr):
    res=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            res.append(-1)
        elif arr[i]>stack[-1][0]:
            res.append(stack[-1][1])
        elif len(stack)!=0 and arr[i]<=stack[-1][0]:
            while len(stack)!=0 and arr[i]<=stack[-1][0]:
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append([arr[i],i])
    return (res[::-1])


def maxAreaHistogram(arr):
    arr.append(0)
    leftWindow=(nextSmallestLeftIndex(arr))
    rightWindow=nextSmallestRightIndex(arr)
    newWindow=[0]*(len(leftWindow)-1)
    for i in range(len(leftWindow)-1):
        newWindow[i]=rightWindow[i]-leftWindow[i]-1

    maxRes=0
    for i in range(len(arr)-1):
        maxRes=max(maxRes,arr[i]*newWindow[i])
    return (maxRes)



height=[6,2,5,4,5,1,6]
#maxAreaHistogram(height)


def rainWaterTrapping(arr):
    maxLeft=[0]*len(arr)
    maxRight=[0]*len(arr)
    maxLeft[0]=arr[0]
    maxRight[len(arr)-1]=arr[len(arr)-1]
    for i in range(1,len(arr)):
        maxLeft[i]=max(maxLeft[i-1],arr[i])
    for j in range(len(arr)-2,-1,-1):
        maxRight[j]=max(maxRight[j+1],arr[j])

    totalWater=0
    for i in range(len(arr)):
        totalWater+=(min(maxLeft[i],maxRight[i])-arr[i])

    print(totalWater)


#rainWaterTrapping([0,1,0,2,1,0,1,3,2,1,2,1])

def maximimumAreainBoinarMatrix(matrix):
    maxArea=0
    vector=[0]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='0':
                vector[j]=0
            else:
                vector[j]+=int(matrix[i][j])
        res=maxAreaHistogram(vector)
        maxArea=max(maxArea,res)
    return maxArea


matrix=[
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
print(maximimumAreainBoinarMatrix(matrix))


