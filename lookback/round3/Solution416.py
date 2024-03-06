#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/12 22:02
# @Author      : Jim
# @File        : Solution416.py
# @Software    : PyCharm
# @Description : 基础算法-动态规划
# 0-1问题的转化


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        dp = []
        N = len(nums)
        total = sum(nums)
        half = total // 2

        if total % 2 != 0:
            return False

        dp = [[0 for i in range(half + 1)] for j in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, half + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j],
                                   dp[i - 1][j - nums[i - 1]] + nums[i - 1]
                                   )

        return half == dp[-1][-1]