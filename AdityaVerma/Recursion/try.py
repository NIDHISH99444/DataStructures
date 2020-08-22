def subs(input,k, index,path, final):
    if k==0:
        final.append(path)
        return
    for i in range(index, len(input)):
        subs(input,k-1, i + 1, path + [input[i]], final)


def subsets( n,k):
    res=[]
    final=[]
    for i in range(1,n+1):
        res.append(i)

    subs(res,k, 0, [], final)
    return final




print(subsets(1,1))