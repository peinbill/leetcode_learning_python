#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/9 23:36
# @Author      : Jim
# @File        : LSolution125.py
# @Software    : PyCharm
# @Description : 基础算法-动态规划
# 0-1 背包问题


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
        N = len(a)

        dp = [[0] * (m + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, m + 1):
                if j - a[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], v[i - 1] + dp[i - 1][j - a[i - 1]])

        return dp[N][m]