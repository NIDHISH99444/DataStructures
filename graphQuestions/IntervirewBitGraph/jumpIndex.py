def canJump(A):
    listIndex = len(A) - 1
    j = len(A) - 2
    while j >= 0:
        if j + A[j] >= listIndex:
            listIndex = j
        j -= 1
    return listIndex == 0


arr=[10,0,1,1,0]
print(canJump(arr))