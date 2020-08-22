import sys


class Solution(object):
    def __init__(self):
        self.max_len = 0
        self.table = {}

    def longestincreasingpath(self, mat):
        def dfs(x, y, prev):
            if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]) or mat[x][y] <= prev:
                return 0
            if (x, y) in self.table:
                return self.table[(x, y)]
            path = 1 + max(dfs(x + 1, y, mat[x][y]), dfs(x - 1, y, mat[x][y]), dfs(x, y + 1, mat[x][y]),
                           dfs(x, y - 1, mat[x][y]))

            self.max_len = max(self.max_len, path)
            self.table[(x, y)] = path

            return path

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dfs(i, j, -sys.maxsize)
        return self.max_len


matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
s = Solution()
print(s.longestincreasingpath(matrix))
