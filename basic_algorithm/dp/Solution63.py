
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        result = [[0 for i in range(n)] for j in range(m)]

        if obstacleGrid[0][0]==1:
            result[0][0] = 0
        else:
            result[0][0] = 1

        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                result[i][0] = 0
            else:
                result[i][0] = result[i-1][0]

        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                result[0][i] = 0
            else:
                result[0][i] = result[0][i-1]


        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
                else:
                    result[i][j] = result[i-1][j]+result[i][j-1]
        return result[-1][-1]


