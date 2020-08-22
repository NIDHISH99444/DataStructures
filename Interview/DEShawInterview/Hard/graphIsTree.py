#https://www.youtube.com/watch?v=vXrv3kruvwE

from collections import defaultdict
class Graph():

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self,sv, visited ):
        queue=[]
        queue.append(sv)
        while queue:
            ele=queue.pop(0)
            visited[ele]=1
            for i in self.graph[ele]:
                if visited[i]==0:
                    return True
                if visited[i]==1:
                    continue
                if visited[i]==-1:
                    queue.append(i)
                    visited[i]=0
        return False


n=5
g2 = Graph()
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
visited=[-1]*n
if g2.isCyclicUtil(0,visited) :
    print("Graph is not a tree,as cycle exists ")
else:
    print("Graph is a Tree ")




