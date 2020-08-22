from collections import defaultdict
import sys


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def check(self, i, visited,graph,cnt,A,res,node):
        visited[i] = True


        for ele in graph[i]:
            if visited[ele] == False:
                cnt += 1
                self.check(ele, visited, graph,cnt,A,res,node)

        if res[0]<cnt:
            res[0]=cnt
            node[0]=i


    def solve(self, A):
        sys.setrecursionlimit(10 ** 6)
        graph = defaultdict(list)
        for i in range(0,len(A)):
            if A[i]==-1:
                root=i
            else:
                graph[i].append(A[i])
                graph[A[i]].append(i)
        node=[0]
        visited = [False] * len(A)
        cnt,res=0,[0]
        if len(graph)==0:
            return 0
        self.check(root, visited, graph,cnt,A,res,node)
        #print(res[0],node[0])
        res=[0]
        visited = [False] * len(A)
        self.check(node[0], visited, graph, cnt, A, res, node)
        return (res[0])


#A=5
A = [-1,0,0,0,3]
# B =[
#   [0, 1],
#   [0, 2],
#   [0, 3],
#   [3, 4],
# ]

s=Solution()
print(s.solve(A))
#print(Solution.solve(A,B))