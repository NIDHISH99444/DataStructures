


from collections import defaultdict
 
def canFinish( numCourses, prerequisites):
        indegree=[0]*numCourses
        graph=defaultdict(list)
        for ele in prerequisites:
            key,val=ele
            graph[key].append(val)

        print(graph)

        for i in range(numCourses):
            for ele in graph[i]:
                indegree[ele]+=1
        print(indegree)
        q=[]
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        if not q: 
            return False
        res=[]
        while q: 
            ele=q.pop(0)
            res.append(ele)
            for neighbour in graph[ele]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        if len(res)==numCourses:
            return True
 
 
if __name__ == "__main__":
    n = 2 # Number of nodes
 
    # Edges
    edges = [[1,0],[0,1]]

    result = canFinish(n,edges)
    print(result)
 


