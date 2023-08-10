
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0 for i in range(n)] for j in range(m)]
        result[0][0] = 1
        for i in range(1,m):
            result[i][0] = 1
        for i in range(1,n):
            result[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                result[i][j] = result[i-1][j]+result[i][j-1]

        return result[-1][-1]