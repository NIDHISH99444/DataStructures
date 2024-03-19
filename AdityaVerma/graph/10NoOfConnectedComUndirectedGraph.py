


from collections import defaultdict

def dfs(visited,graph,node):
    visited[node]=True
    for neighbour in graph[node]:
        if visited[neighbour]!=True:
            dfs(visited,graph,neighbour)
 
def canFinish( n, prerequisites):
    graph = defaultdict(list)

    for ele in prerequisites:
        key,val=ele
        graph[key].append(val)
        graph[val].append(key)


    visited=[False]*n
    cnt=0
    for i in range(n):
        if visited[i]!=True:
            dfs(visited,graph,i)
            cnt+=1
            
    return cnt
    


if __name__ == "__main__":
    n = 3 # Number of nodes
 
    # Edges
    # edges = [[3,2],[2,1],[1,0]]
    edges = [[0,1], [0,2]]

    result = canFinish(n,edges)
    print(result)
 


