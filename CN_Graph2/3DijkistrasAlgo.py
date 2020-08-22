# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
# Print the ith vertex number and the distance from source in one line separated by space. Print different vertices in different lines.
# Note : Order of vertices in output doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# In different lines, ith vertex number and its distance from source (separated by space)
# Constraints :
# 2 <= V, E <= 10^5
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 0
# 1 3
# 2 4
# 3 5
import  sys
def getMinVertex(weight,visited,n):
    minVertex=-1
    for i in range(n):
        if visited[i]==False and (minVertex==-1 or weight[minVertex]>weight[i]):
            minVertex=i
    return minVertex
def prims(edges,n):
    visited=[False]*n

    weight=[sys.maxsize]*n
    weight[0]=0
    for i in range(0,n-1):
        #get minVertex from unvisited vertices
        minVertex=getMinVertex(weight,visited,n)
        visited[minVertex]=True
        #explore all the neighbour of minVertex and update parent and weight according to that
        for j in range(n):
            if edge[minVertex][j]!=0 and visited[j]==False:
                if weight[j]>weight[minVertex]+edge[minVertex][j]:
                    weight[j]=weight[minVertex]+edge[minVertex][j]
    for i in range(n):
        print(i,weight[i])



#
n,m=4,4
interval=[[0, 1, 3], [0, 3, 5], [1, 2, 1], [2, 3, 8]]
# interval=[]
# n,m=list(map(int,input().split()))
edge=[[0 for i in range(n)]for j in range(n)]
#
# for i in range(m):
#     lst=list(map(int,input().split()))
#     interval.append(lst)

for i in range(len(interval)):
    edge[interval[i][0]][interval[i][1]]=interval[i][2]
    edge[interval[i][1]][interval[i][0]] = interval[i][2]

prims(edge,n)


