class Solution:
    # @param A : list of strings
    # @return an integer
    def dfs(self,graph,i,j,cnt):
        if i<0 or i>=len(graph) or j<0 or j>=len(graph[0]) or graph[i][j]=='O':
            return
        if graph[i][j]=='X':
            graph[i][j]='O'

        rowNbr = [-1, 0,1, 0]
        colNbr = [0, 1 ,0, -1]
        for s in range(len(rowNbr)):
            self.dfs(graph,i+rowNbr[s],j+colNbr[s],cnt)
    def black(self, graph):
        res,ll=[],[]
        for ele in graph:
            for val in ele:
                res.append(val)
            ll.append(res)
            res=[]
        graph=ll

        cnt=0
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j]=='X':

                    self.dfs(graph,i,j,cnt)
                    cnt+=1

        return cnt
s=Solution()
A = [ "XXX", "XXX", "XXX" ]
print(s.black(A))