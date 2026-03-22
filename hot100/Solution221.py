from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, ch in enumerate(row):
                if ch == '1':
                    f[i + 1][j + 1] = min(f[i][j], f[i][j + 1], f[i + 1][j]) + 1
        return max(map(max, f)) ** 2

