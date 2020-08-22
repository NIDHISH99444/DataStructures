from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)



    def dfsutil(self,v,visited,res):
        visited[v]=True

        for i in self.graph[v]:
            if visited[i]==False:
                self.dfsutil(i,visited,res)
        res.insert(0,v)
    def dfs(self):
        visited=[0]*self.vertices
        res=[]
        for i in range(self.vertices):
            if visited[i]==False:
                self.dfsutil(i,visited,res)
        print(res)

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)



g.dfs()
