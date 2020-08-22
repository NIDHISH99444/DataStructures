def getParent(v,parent):
    if parent[v]==v:
        return v
    return getParent(parent[v],parent)

def kruskal(interval,n,e):

    parent = [0] * n
    for i in range(n):
        parent[i] = i

    count=0
    i=0
    while count<n-1:

        startParent=getParent(interval[i][0],parent)
        endParent=getParent(interval[i][1],parent)
        if startParent!=endParent:
            count+=1
            output.append(interval[i])
            parent[startParent]=endParent
        i+=1


def sortAccordingToWeight(interval):
    interval=sorted(interval,key=lambda x:x[2])
    return (interval)
n,e=4,5
interval=[[0, 1, 10], [1, 3, 15], [0, 3, 5], [0, 2, 6],[2,3,4]]
# interval=[]
# n,m=list(map(int,input().split()))
# for i in range(m):
#      lst=list(map(int,input().split()))
#      interval.append(lst)
#print(interval)
interval=sortAccordingToWeight(interval)
output = []
kruskal(interval,n,e)

output=sorted(output,key=lambda x:x[2])



for ele in output:
    if ele[0]>ele[1]:
        ele[0],ele[1]=ele[1],ele[0]
for ele in output:
    for e in ele:
        print(e,end=" ")
    print()


