from _collections import defaultdict
class Graph:

    def __init__(self,m):
        self.graph=defaultdict(list)
        self.vertices=m
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfsutil(self,v,visited,res):
        visited[v]=True
        res.append(v)
        for ele in self.graph:
            if visited[ele]==False:
                self.dfsutil(ele,visited,res)
    def dfs(self,cli,croad):
        if croad>cli:
            return cli*self.vertices

        visited=[0]*self.vertices
        res=[]
        val=0

        for i in range(self.vertices):

            if visited[i]==False:
                self.dfsutil(i,visited,res)
                val+=(len(res)-1)*croad+cli
            res=[]
        return val




m,n,cli,croad=6,6,2,1
g=Graph(m)

g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(2,4)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(5,6)
print(g.dfs(cli,croad))



