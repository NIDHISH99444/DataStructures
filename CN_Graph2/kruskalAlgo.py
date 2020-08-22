# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.
# For printing MST follow the steps -
# 1. In one line, print an edge which is part of MST in the format -
# v1 v2 w
# where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1 <= v2 i.e. print the smaller vertex first while printing an edge.
# 2. Print V-1 edges in above format in different lines.
# Note : Order of different edges doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# MST
# Constraints :
# 2 <= V, E <= 10^5
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 1 2 1
# 0 1 3
# 0 3 5

def getParent(v,parent):
    if parent[v]==v:
        return v
    return getParent(parent[v],parent)

def kruskal(interval,vertices,edges):

    parent = [0] * edges
    for i in range(edges):
        parent[i] = i

    count=0
    i=0
    while count<vertices-1:

        startParent=getParent(interval[i][0],parent)
        endParent=getParent(interval[i][1],parent)
        if startParent!=endParent:
            count+=1
            output.append(interval[i])
            parent[startParent]=endParent
        i+=1


def sortAccordingToWeight(interval):
    interval=sorted(interval,key=lambda x:x[2])
    return (interval)
vertices,edges=4,5
interval=[[0, 1, 10], [0, 3, 5], [0, 2, 6], [1, 3, 15],[2,3,4]]
# interval=[]
# n,m=list(map(int,input().split()))
# for i in range(m):
#      lst=list(map(int,input().split()))
#      interval.append(lst)
#print(interval)
interval=sortAccordingToWeight(interval)
output = []
kruskal(interval,vertices,edges)

output=sorted(output,key=lambda x:x[2])



for ele in output:
    if ele[0]>ele[1]:
        ele[0],ele[1]=ele[1],ele[0]
for ele in output:
    for e in ele:
        print(e,end=" ")
    print()


