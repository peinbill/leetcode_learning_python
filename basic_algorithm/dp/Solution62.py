
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = [[0 for i in range(n)] for j in range(m)]
        result[0][0] = grid[0][0]

        for i in range(1, m):
            result[i][0] = result[i - 1][0] + grid[i][0]

        for i in range(1, n):
            result[0][i] = result[0][i - 1] + grid[0][i]

        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = min(result[i - 1][j], result[i][j - 1]) + grid[i][j]

        return result[-1][-1]