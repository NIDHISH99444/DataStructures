# Monk visits the land of Islands. There are a total of N islands numbered from 1 to N. Some pairs of islands are connected to each other by Bidirectional bridges running over water.
# Monk hates to cross these bridges as they require a lot of efforts. He is standing at Island #1 and wants to reach the Island #N. Find the minimum the number of bridges that he shall have to cross, if he takes the optimal route.
# Input:
# First line contains T. T testcases follow.
# First line of each test case contains two space-separated integers N, M.
# Each of the next M lines contains two space-separated integers X and Y , denoting that there is a bridge between Island X and Island Y.
# Output:
# Print the answer to each test case in a new line.
# Constraints:
# 1 ≤ T ≤ 10
# 1 ≤ N ≤ 10000
# 1 ≤ M ≤ 100000
# 1 ≤ X, Y ≤ N
# SAMPLE INPUT
# 2

# 3 2
# 1 2
# 2 3

# 4 4
# 1 2
# 2 3
# 3 4
# 4 2
# SAMPLE OUTPUT
# 2
# 2

from collections import defaultdict


# are you able to see my writing? Reply on chatbox
def bfs(graph, sv, ev, count):
    pendingVertices = []
    pendingVertices.append(sv)
    visited[sv] = True
    count[sv] = 0
    # pass
    while pendingVertices:  # acting as the queue correct
        currVertice = pendingVertices.pop(0)  # front of the queue you are taking correct
        for i in graph[currVertice]:
            if visited[i] == False:  # if the adjacent node not visited mark it visited correct
                visited[i] = True  # correct
                count[i] = count[currVertice] + 1  # you are storing what it will do?
                pendingVertices.append(i)
            if i == ev:
                return (count[i])


def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)


tstcases = int(input())
for i in range(tstcases):
    graph = defaultdict(list)
    n, edge = list(map(int, input().split()))
    for i in range(edge):
        p, q = list(map(int, input().split()))
        addEdge(p, q)

    visited = [False] * (n + 1)

    count = [-1] * (n + 1)
    start = 1
    end = n
    print(bfs(graph, start, end, count))
