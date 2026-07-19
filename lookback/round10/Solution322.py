#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/19 00:39
# @Author      : Jim
# @File        : Solution322.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[ float("inf") for i in range(amount+1)] for _ in range(len(coins)+1)]
        m = len(dp)
        n = len(dp[0])
        for i in range(m):
            dp[i][0] = 0

        for i in range(1,m):
            for j in range(1,n):
                if coins[i-1]<=j:
                    dp[i][j] = min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        if dp[-1][-1] == float("inf"):
            return -1
        else:
            return dp[-1][-1]