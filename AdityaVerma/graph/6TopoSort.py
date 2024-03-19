



 
def topological_sort(graph, V):
    indegree=[0]*V
    for i in range(V):
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
    return res

 
 
if __name__ == "__main__":
    n = 4  # Number of nodes
 
    # Edges
    edges = [[0, 1], [1, 2], [3, 1], [3, 2]]
 
    # Graph represented as an adjacency list
    adj = [[] for _ in range(n)]
 
    # Constructing adjacency list
    for edge in edges:
        adj[edge[0]].append(edge[1])
 
    
    
    result = topological_sort(adj, n)
    print(result)
 


