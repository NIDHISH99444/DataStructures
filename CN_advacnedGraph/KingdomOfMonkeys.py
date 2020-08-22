from _collections import  defaultdict
class Graph:


    def dfs(self,i,visited,adj,arr,res):
        visited[i]=True
        res[0]+=arr[i]
        for ele in adj[i]:
            if visited[ele]==False:
                self.dfs(ele,visited,adj,arr,res)

g=Graph()

t=int(input())
while t>0:

    n,e=map(int,input().split())
    visited = [False] * n
    adj=defaultdict(list)
    for i in range(e):
        a,b=map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    arr=list(map(int,input().split()))
    max=0
    h=0
    for i in range(n):
        if visited[i]==False:
            res=0
            g.dfs(i,visited,adj,arr,res)
            if res>max:
                max=res
    print(max)
    t-=1

# n,e=4,3
# adj=defaultdict(list)
# adj[0].append(1)
# adj[1].append(0)
# adj[1].append(2)
# adj[2].append(1)
# adj[2].append(0)
# adj[0].append(2)
#
# arr=[1,2,3,5]
# visited=[False]*n
# max=0
# for i in range(n):
#     if visited[i]==False:
#         res=[0]
#         g.dfs(i,visited,adj,arr,res)
#         if res[0]>max:
#             max=res[0]
#
# print(max)

