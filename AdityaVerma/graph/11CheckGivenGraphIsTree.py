


from collections import defaultdict
# this question is answer to "Detect cycle in undirected graph" using DFS

# here we have to check 2 thing 
# -> it should not have cycle 
#-> all componetns are connnected
 
def dfs(graph,node,parent,visited):
    visited[node]=True
    for neighbour in graph[node]:
        if visited[neighbour]==False:
            return dfs(graph,neighbour,node,visited)
        elif  parent!=neighbour:
            return True
    return False


def canFinish( n, prerequisites):
    graph = defaultdict(list)

    for ele in prerequisites:
        key,val=ele
        graph[key].append(val)
        graph[val].append(key)

    visited=[False]*n
    
    for i in range(n):
        if visited[i]==False:
            if dfs(graph,i,-1,visited):
                return True
        return False
    # for ele in visited:
    #     if ele==False:
    #         return False
    # return True
    

    


if __name__ == "__main__":
    n = 5 
    edges = [[1,0], [0,2],[2,0],[3,0],[3,4]]

    result = canFinish(n,edges)
    print(result)
 


