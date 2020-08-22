class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.supStack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack)==0:
            self.stack.append(x)
            self.supStack.append(x)
        else:
            self.stack.append(x)
            if self.supStack[-1]>=self.stack[-1]:
                self.supStack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack)==0:
            return -1
        else:
            if self.stack[-1]>self.supStack[-1]:
                self.stack.pop()
            else:
                self.stack.pop()
                self.supStack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return -1
        else:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.supStack)==0:
            return -1
        else:
            return self.supStack[-1]

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)
print(minStack.getMin())  #return -3
minStack.pop()
#print(minStack.top())  # return 0
print(minStack.getMin())

# ["MinStack","push","push","push","getMin","pop","getMin"]
# [[],[0],[1],[0],[],[],[]]