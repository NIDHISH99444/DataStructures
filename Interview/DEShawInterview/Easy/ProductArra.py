def product(arr):
    p=1
    res=[]
    for i in range(len(arr)):
        res.append(p)
        p*=arr[i]
    print(res)
    p=1
    for i in range(len(arr)-1,-1,-1):
        res[i]*=p
        p*=arr[i]
    print(res)


product([10, 3, 5, 6, 2])