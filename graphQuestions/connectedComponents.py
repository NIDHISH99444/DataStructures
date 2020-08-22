from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfsutil(self,v,visited,res):
        visited[v]=True
        res.append(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.dfsutil(i,visited,res)
    def dfs(self):
        visited=[0]*self.vertices
        res=[]
        for i in range(self.vertices):
            if visited[i]==False:
                self.dfsutil(i,visited,res)
                print(res)
            res=[]
g=Graph(5)
g.addEdge(0,1)
g.addEdge(3,2)
g.addEdge(3,4)

g.dfs()
