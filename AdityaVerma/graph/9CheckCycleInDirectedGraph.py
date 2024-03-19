


from collections import defaultdict
# This 
def dfs(visited,recStack,graph,node):
    visited[node]=True
    recStack[node]=True
    for neighbour in graph[node]:
        if visited[neighbour]==False:
            return dfs(visited,recStack,graph,neighbour)
        elif recStack[neighbour]==True:
            return True
    recStack[node]=False
    return False
 
def canFinish( numCourses, prerequisites):
    graph = defaultdict(list)

    for ele in prerequisites:
        key,val=ele
        graph[key].append(val)

    visited=[False]*numCourses
    recStack=[False]*numCourses

    for i in range(numCourses):
        if visited[i]!=True:
            if dfs(visited,recStack,graph,i):
                return True
    return False
           
    
    


if __name__ == "__main__":
    n = 2 # Number of nodes
 
    # Edges
    # edges = [[3,2],[2,1],[1,0]]
    edges = [[1,0],[0,1]]

    result = canFinish(n,edges)
    print(result)
 


