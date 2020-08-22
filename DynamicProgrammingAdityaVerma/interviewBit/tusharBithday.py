def solve( R, A):
    smallest = float('inf')
    k = 0
    for i in range(len(A)):
        if A[i] < smallest:
            smallest = A[i]
            k = i
    tolerance = R % smallest
    res = [k] * (R // smallest)
    i = 0
    j = 0
    while j < k and i < len(res):
        if A[j] - smallest <= tolerance:
            res[i] = j
            tolerance -= A[j] - smallest
            i += 1
        else:
            j += 1
    return res
A = 11
B = [6, 8, 5, 4, 7]
print(solve(A,B))