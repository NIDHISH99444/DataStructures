import heapq


def findkthsmallest(mat, k):
    arr, res = [], None
    heapq.heappush(arr, (mat[0][0], 0, 0))
    while k > 0:
        res, i, j = heapq.heappop(arr)
        if i == 0 and j < len(mat[0]) - 1:
            heapq.heappush(arr, (mat[i][j + 1], i, j + 1))
        if i < len(mat) - 1:
            heapq.heappush(arr, (mat[i + 1][j], i + 1, j))
        k -= 1
    return res


matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
print(findkthsmallest(matrix, 3))
