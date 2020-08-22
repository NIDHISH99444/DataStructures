from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def addEdge(u,v):
    graph[u].append(v)

def dfsutil(v,visited,res):
    visited[v]=True
    res.append(v)
    for ele in graph:
        if visited[ele]==False:
            dfsutil(ele,visited,res)

def roadsAndLibraries(n, cli, croad, cities):
    for ele in cities:
        addEdge(ele[0],ele[1])
    if croad>cli:
        return cli*n

    visited=[0]*n
    res=[]
    val=0

    for i in range(n):

        if visited[i]==False:
            dfsutil(i,visited,res)
            val+=(len(res)-1)*croad+cli
        res=[]
    return val



if __name__ == '__main__':

    #
    # q = int(raw_input())
    #
    # for q_itr in xrange(q):
    #     nmC_libC_road = raw_input().split()
    #
    #     n = int(nmC_libC_road[0])
    #
    #     m = int(nmC_libC_road[1])
    #
    #     c_lib = int(nmC_libC_road[2])
    #
    #     c_road = int(nmC_libC_road[3])
    #
    #     cities = []

        n,m,cli,croad=6,6,2,1

        cities=[(1,3),(3,4),(2,4),(1,2),(2,3),(5,6)]
        # for _ in range(m):
        #     cities.append(map(int, raw_input().rstrip().split()))
        graph=defaultdict(list)
        result = roadsAndLibraries(n, cli, croad, cities)
        print(result)