# Python program to detect cycle
# in a graph

from collections import defaultdict
class Graph():
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def isCyclicUtil(self, v, visited,):
		visited[v] = True
		for neighbour in self.graph[v]:
			if visited[neighbour] == False:
				self.isCyclicUtil(neighbour, visited)


	# Returns true if graph is cyclic else false
	def isPath(self,start,end):

		self.isCyclicUtil(start,visited)
		return visited[end]




g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)

start=1
end= 5
visited = [False] * (end+1)
if (g.isPath(start,end))==False:
	print(0)
else:
	print(1)

