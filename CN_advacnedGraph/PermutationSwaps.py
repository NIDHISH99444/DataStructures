from _collections import  defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)


    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfsUtil(self,v,visited,res):

        visited[v]=True
        res.append(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.dfsUtil(i,visited,res)

    def dfs(self,n):
        ll=[]
        visited=[False]*n
        for i in range(n):
            if visited[i]==False:
                res=[]
                self.dfsUtil(i,visited,res)
                res.sort()
                ll.append(res)

        return  ll


g=Graph()
# n=4
# p=[0,2,1,3]
# q=[0,3,1,2]
# # [1 ,3 ,2 ,4]
# # [1 ,4 ,2 ,3]
# g.addEdge(2, 3)
#
#
#
# print("checking DFS order")
# ll=g.dfs(n)


t=int(input())
while t>0:
    graph = defaultdict(list)
    n,e=map(int,input().split())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))

    while e>0:
        u,v=map(int,input().split())
        g.addEdge(u-1,v-1)
        e-=1
    for i in range(len(p)):
        p[i]-=1
    for j in range(len(q)):
        q[j]-=1

    ll = g.dfs(n)
    graph = defaultdict(list)

    flag=0
    for ele in ll:
        setP=set([])
        setQ=set([])
        for item in ele:
            setP.add(p[item])
            setQ.add(q[item])
        if setP!=setQ:
            flag=1
            break

    if flag==0:
        print("YES")
    else:
        print("NO")
    ll=[]
    t-=1

#
#
#
# n,e=4,1
# p=[1, 3 ,2 ,4]
# q=[1 ,4 ,2 ,3]
#
# while e>0:
#     u,v=3,4
#     g.addEdge(u-1,v-1)
#     e-=1
# for i in range(len(p)):
#     p[i]-=1
# for j in range(len(q)):
#     q[j]-=1
#
# ll = g.dfs(n)
# graph = defaultdict(list)
#
# flag=0
# for ele in ll:
#     setP=set([])
#     setQ=set([])
#     for item in ele:
#         setP.add(p[item])
#         setQ.add(q[item])
#     if setP!=setQ:
#         flag=1
#         break
#
# if flag==0:
#     print("YES")
# else:
#     print("NO")
# ll=[]
# p=[1, 3 ,2 ,4]
# q=[1 ,4 ,2 ,3]
#
# while e>0:
#     u,v=2,4
#     g.addEdge(u-1,v-1)
#     e-=1
# for i in range(len(p)):
#     p[i]-=1
# for j in range(len(q)):
#     q[j]-=1
#
# ll = g.dfs(n)
#
#
# flag=0
# for ele in ll:
#     setP=set([])
#     setQ=set([])
#     for item in ele:
#         setP.add(p[item])
#         setQ.add(q[item])
#     if setP!=setQ:
#         flag=1
#         break
#
# if flag==0:
#     print("YES")
# else:
#     print("NO")
# ll=[]


# 2
# 4 1
# 1 3 2 4
# 1 4 2 3
# 3 4
# 4 1
# 1 3 2 4
# 1 4 2 3
# 2 4