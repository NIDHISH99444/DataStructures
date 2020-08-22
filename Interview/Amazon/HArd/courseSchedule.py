#using topologicalSort
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.v=vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,v,visited,stack):
        visited[v]=True

        for i in self.graph[v]:
            if visited[i]==False:
                self.dfs(i,visited,stack)
        stack.append(v)

    def topologicalSort(self):
        visited=[0]*self.v
        stack=[]
        for i in range(self.v):
            if visited[i]==False:
                self.dfs(i,visited,stack)
        return stack

numCourses=4
prerequisites=[[1,0],[2,0],[3,1],[3,2]]

g=Graph(numCourses)
for ele in prerequisites:
    g.addEdge(ele[0],ele[1])
# g.addEdge(1,0)
# g.addEdge(2,0)
# g.addEdge(3,1)
# g.addEdge(3,2)

stack=g.topologicalSort()
print(stack)