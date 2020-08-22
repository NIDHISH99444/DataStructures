from collections import defaultdict
import sys


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def check(self, i, visited,graph,cnt,A,C,res):
        visited[i] = True
        if A[i-1]==1:
            cnt+=1
        flag=False
        for ele in graph[i]:
            flag=True
            if visited[ele] == False:
                self.check(ele, visited, graph,cnt,A,C,res)
        if cnt<=C and flag==False:
            res[0]+=1


    def solve(self, A, B,C):
        sys.setrecursionlimit(10 ** 6)
        graph = defaultdict(list)
        for ele in B:
            if ele[0]<ele[1]:
                graph[ele[0]].append(ele[1])
            else:
                graph[ele[1]].append(ele[0])
        visited = [False] * (len(A)+1)
        cnt,res=0,[0]
        self.check(1, visited, graph,cnt,A,C,res)
        print (res[0])




A =[ 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1 ]
B =[
  [10, 6],
  [3, 2],
  [12, 7],
  [9, 5],
  [2, 1],
  [8, 3],
  [7, 1],
  [4, 2],
  [6, 3],
  [11, 4],
  [5, 3],
  [13, 11]
]
C = 7
s=Solution()
s.solve(A,B,C)
#print(Solution.solve(A,B))