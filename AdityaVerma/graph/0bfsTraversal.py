from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)

    def addEdge(self,u, v):
        self.graph[u].append(v)

    
    def bfs(self,node,n):
        vis=[False]*n
        q=[]
        q.append(node)
        vis[node]=True
        while q : 
            node=q.pop(0)
            print(node)
            for neighbour in self.graph[node]:
                if vis[neighbour]==False:
                    q.append(neighbour)
                    vis[neighbour]=True
            





graph = Graph()
 
n=5
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 4)
graph.addEdge(3, 4)

graph.bfs(0,n)