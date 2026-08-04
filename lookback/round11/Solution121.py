#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/4 08:27
# @Author      : Jim
# @File        : Solution121.py
# @Software    : PyCharm
# @Description :
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit