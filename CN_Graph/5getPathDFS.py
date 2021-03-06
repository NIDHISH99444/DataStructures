# Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
# Find the path using DFS and print the first path that you encountered.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
# Note : Save the input graph in Adjacency Matrix.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Two integers a and b, denoting that there exists an edge between vertex a and vertex b (separated by space)
# Line (E+2) : Two integers v1 and v2 (separated by space)
# Output Format :
# Path from v1 to v2 in reverse order (separated by space)
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# 0 <= v1, v2 <= V-1
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# 3 0 1
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3     (start ,end)
def dfs(edge,n,visited,sv,end,mp):
    visited[sv]=True
    for i in range(n):
        if i ==sv:
            continue
        elif edges[sv][i]==1 and visited[i]==False:
                mp[i]=sv
                dfs(edges,n,visited,i,end,mp)

def addEdge(u,v):
    edges[u][v]=1
    edges[v][u]=1



n,edge=4,4
edges=[[0 for i in range(n)]for j in range(n)]
addEdge(0,1)
addEdge(0,3)
addEdge(1,2)
addEdge(2,3)
start,end=1,3

print(edges)
visited=[False]*n
mp={}
dfs(edges,n,visited,start,end,mp)
print(mp)

def printPath(mp, start, end):
    if end not in mp:
        return
    else:
        print(end, end=" ")
        while end != start:
            print(mp[end], end=" ")
            end = mp[end]


printPath(mp, start, end)

