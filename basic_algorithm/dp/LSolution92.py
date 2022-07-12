from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack2(self, m: int, a: List[int]) -> int:
        """ 当不限选择的时候

        :param m:
        :param a:
        :return:
        """
        # write your code here
        dp = [-float("inf") for _ in range(m+1)]
        dp[0] = 0


        for i in range(1,len(dp)):
            for j in a:
                if i-j>=0 and dp[i-j] != -float("inf"):
                    dp[i] = max(dp[i-j]+j,dp[i])

        return max(dp)

    def backPack(self, m, A):

        n = len(A)

        if sum(A) <= m:

            return sum(A)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] > j:

                    dp[i][j] = dp[i - 1][j]

                else:

                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])

        return dp[n][m]