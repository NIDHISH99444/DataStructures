from _collections import  defaultdict
class Graph:
    def __init__(self,n):
        self.graph=defaultdict(list)
        self.n=n

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfsUtil(self,v,visited,res):

        visited[v]=True
        res.append(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.dfsUtil(i,visited,res)

    def dfs(self):
        visited=[False]*self.n
        for i in range(self.n):
            if visited[i]==False:
                res=[]
                self.dfsUtil(i,visited,res)
                res.sort()
                for ele in res:
                    print(ele,end=" ")
                print()
n=5
g=Graph(n)
g.addEdge(0, 1)
g.addEdge(3, 2)
g.addEdge(3, 4)

# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
print("checking DFS order")
g.dfs()