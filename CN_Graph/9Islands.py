# An island is a small piece of land surrounded by water . A group of islands is said to be connected if we can reach from any given island to any other island in the same group . Given N islands (numbered from 1 to N) and two lists of size M (u and v) denoting island u[i] is connected to island v[i] and vice versa . Can you count the number of connected groups of islands.
# Constraints :
# 1<=N<=100
# 1<=M<=(N*(N-1))/2
# 1<=u[i],v[i]<=N
# Input Format :
# Line 1 : Two integers N and M
# Line 2 : List u of size of M
# Line 3 : List v of size of M
# Output Return Format :
# The count the number of connected groups of islands
# Sample Input :
# 2 1
# 1
# 2
# Sample Output :
# 1

def addEdge(u,v):
    edges[u][v]=1
    edges[v][u]=1
def dfsUtil(edge,n,visited,sv,res):
    res.append(sv)
    visited[sv]=True
    for i in range(n):
        if i ==sv:
            continue
        elif edges[sv][i]==1:
            if visited[i]==True:
                continue
            else:
                dfsUtil(edges,n,visited,i,res)

def dfs(edge,n):
    for i in range(n):
        visited=[False]*n
    cnt=0
    for i in range(n):
        if visited[i]==False:
            res=[]
            dfsUtil(edge,n,visited,i,res)
            cnt+=1
    return cnt

n,m=list(map(int,input().split()))
edges=[[0 for i in range(n)]for j in range(n)]
visited=[False]*n

u=list(map(int,input().split()))
v=list(map(int,input().split()))
for i in range(m):
    addEdge(u[i]-1,v[i]-1)


print(dfs(edges,n))
