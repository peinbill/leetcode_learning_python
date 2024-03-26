#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/13 22:32
# @Author      : Jim
# @File        : Solution121.py
# @Software    : PyCharm
# @Description :


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 暴力破解

        @param prices:
        @return:
        """
        dp = [0 for i in prices]

        for i in range(1,len(prices)):
            for j in range(i-1,-1,-1):
                if prices[i]>prices[j]:
                    dp[i] = max(prices[i]-prices[j]+dp[j],dp[i])

        return max(dp)

    def maxProfit2(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
