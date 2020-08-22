def findParent(v,parent):
    if parent[v]==v:
        return v
    return  findParent(parent[v],parent)

def commutable(A,B):
    parent=[0]*(A+1)
    for i in range(1,A+1):
        parent[i]=i

    count=0
    i=0
    res=0
    while count < A-1:
        start=findParent(B[i][0],parent)
        end=findParent(B[i][1],parent)
        if start!=end:
            count+=1
            parent[start]=end
            res+=B[i][2]
        i+=1

    return res


def sortInterval(interval):
    interval=sorted(interval,key=lambda x:x[2])
    return interval

A = 4
B = [   [1, 2, 1],
        [2, 3, 4],
        [1, 4, 3],
        [4, 3, 2],
        [1, 3, 10]  ]

B=sortInterval(B)

print(commutable(A,B))
