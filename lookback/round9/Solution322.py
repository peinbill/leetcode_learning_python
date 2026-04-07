#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/7 23:55
# @Author      : Jim
# @File        : Solution322.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf") for j in range(amount + 1)] for i in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 0

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)

        if dp[-1][-1] == float("inf"):
            return -1

        return dp[-1][-1]