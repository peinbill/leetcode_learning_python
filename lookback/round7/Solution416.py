#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/15 16:41
# @Author      : Jim
# @File        : Solution416.py
# @Software    : PyCharm
# @Description : 需要考虑放进去和不放进去
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        total = sum(nums)

        if total % 2 != 0:
            return False
        bag = total // 2
        order_nums = sorted(nums)

        dp = [[0 for j in range(bag + 1)] for i in range(len(order_nums) + 1)]
        for row in range(1, len(order_nums) + 1):
            for column in range(1, bag + 1):
                if column - order_nums[row - 1] >= 0:
                    dp[row][column] = max(dp[row - 1][column],
                                          order_nums[row - 1] + dp[row - 1][column - order_nums[row - 1]])
                else:
                    dp[row][column] = dp[row - 1][column]
        return dp[-1][-1] == bag
