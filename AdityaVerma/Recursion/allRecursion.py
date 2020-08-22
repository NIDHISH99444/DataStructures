def print1ton(n):
    if n==0:
        return
    print1ton(n-1)
    print(n,end=" ")

#print1ton(5)
print()
def printnto1(n):
    if n==0:
        return
    print(n,end=" ")
    printnto1(n-1)

#printnto1(6)

def insert(arr,temp):
    if len(arr)==0 or arr[len(arr)-1]<=temp:
        arr.append(temp)
        return
    val=arr.pop()
    insert(arr,temp)
    arr.append(val)
def sortA(arr):
    if len(arr)==1:
        return
    temp=arr.pop()
    sortA(arr)
    insert(arr,temp)



arr=[1,5,4,3]
print("Array after sorting ")
sortA(arr)
print(arr)


def solve(arr,k):
    if k==1:
        arr.pop()
        return
    temp=arr.pop()
    solve(arr,k-1)
    arr.append(temp)

def deleteMiddleStack(arr,n):
    if len(arr)==0:
        return arr
    k=len(arr)//2+1
    print(k)
    solve(arr,k)

stack=[1,2,3,4,5,6]
n=len(stack)
print("After deleting middle of stack ")
deleteMiddleStack(stack,n)
print(stack)

def insertEnd(arr,temp):
    if len(arr)==0:
        arr.append(temp)
        return
    val=arr.pop()
    insertEnd(arr,temp)
    arr.append(val)

def reverseStack(arr):
    if len(arr)==1:
        return
    temp=arr.pop()
    reverseStack(arr)
    insertEnd(arr,temp)


arr=[1,2,3,4]
#reverseStack(arr)
#print(arr)



def solveSubset(input,output,res):
    if len(input)==0:
        res.append(output)
        return
    output1=output
    output2=output+input[0]
    solveSubset(input[1:],output1,res)
    solveSubset(input[1:],output2,res)



input="ab"
output=""
res=[]
print("Print all subsets ")
solveSubset(input,output,res)
print(res)


def permutationWithSpace(input,output,res):
    if len(input)==0:
        res.append(output)
        return
    output1=output+"_"+input[0]
    output2=output+input[0]
    permutationWithSpace(input[1:],output1,res)
    permutationWithSpace(input[1:],output2,res)

def solve(input,output):
    output+=input[0]
    res=[]
    permutationWithSpace(input[1:],output,res)
    print(res)
input="ABC"
output=""
print("Permutation with spaces o/p")
solve(input,output)


def permutationWithCaseChange(input,output,res):
    if len(input)==0:
        res.append(output)
        return
    output1=output+input[0]
    output2=output+input[0].upper()
    permutationWithCaseChange(input[1:],output1,res)
    permutationWithCaseChange(input[1:],output2,res)


input="ab"
output=""
res=[]
permutationWithCaseChange(input,output,res)
print("Permutation with case change o/p")
print(res)

def letterCasePermutation(input,output,res):
    if len(input)==0:
        res.append(output)
        return
    if input[0].isdigit():
        output1=output+input[0]
        letterCasePermutation(input[1:], output1, res)
    else:
        output1=output+input[0]
        output2=output+input[0].upper()
        letterCasePermutation(input[1:],output1,res)
        letterCasePermutation(input[1:],output2,res)

input="3z4"
output=""
res=[]
letterCasePermutation(input,output,res)
print("Letter case permutation o/p")
print(res)