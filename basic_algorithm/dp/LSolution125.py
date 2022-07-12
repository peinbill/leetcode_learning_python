from typing import (
    List,
)


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """

    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        # write your code here

        n = len(a)

        if sum(a) < m:
            return sum(v)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] > j:

                    dp[i][j] = dp[i - 1][j]

                else:

                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + v[i - 1])

        return dp[n][m]