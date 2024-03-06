#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/2/25 23:14
# @Author      : Jim
# @File        : Solution322.py
# @Software    : PyCharm
# @Description :

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        N = len(coins)

        dp = [[float("inf") for j in range(amount + 1)] for i in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 0

        for i in range(1, N + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)

        if dp[-1][-1] == float("inf"):
            return -1
        return dp[-1][-1]