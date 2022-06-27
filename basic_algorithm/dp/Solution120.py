from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])
        result = [[float("inf") for i in range(n)] for j in range(m)]

        result[0][0] = triangle[0][0]
        for i in range(len(triangle)):
            if len(triangle[i]) == 1:
                continue
            for j in range(len(triangle[i])):
                if j == 0:
                    result[i][j] = result[i - 1][j] + triangle[i][j]

                result[i][j] = min(result[i - 1][j], result[i - 1][j - 1]) + triangle[i][j]

        return min(result[-1])
