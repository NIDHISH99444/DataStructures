from collections import defaultdict
import sys


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def check(self, i, visited,graph,recStack):
        visited[i] = True
        recStack[i]=True
        for ele in graph[i]:
            if visited[ele] == False:
                if self.check(ele, visited, graph,recStack)==True:
                    return True
            elif recStack[ele]==True:
                return True
        recStack[i]=False
        return False

    def solve(self, A, B,C):
        sys.setrecursionlimit(10 ** 6)
        graph = defaultdict(list)
        for a, b in zip(B, C):
            graph[a].append(b)
        print(graph)
        recStack=[False] * (A+1)
        visited=[False] * (A+1)
        for i in range(1,A+1):
            if visited[i]==False:
                if self.check(i, visited, graph,recStack)==True:
                    return 0
        return 1



A = 5
B = [ 1, 3, 4, 5 ]
C = [ 2, 1, 5, 3 ]

s=Solution()
print(s.solve(A,B,C))
#print(Solution.solve(A,B))