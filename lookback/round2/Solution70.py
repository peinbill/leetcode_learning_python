#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/1 20:15
# @Author      : Jim
# @File        : Solution70.py
# @Software    : PyCharm
# @Description : 基础算法-动态规划

class Solution:
    def climbStairs(self, n: int) -> int:
        # 序列问题，核心方程式为f(n) = f(n-1) + f(n-2)
        if n == 1:
            return 1

        stairs = [0 for i in range(n + 1)]

        stairs[0] = 1
        stairs[1] = 1

        for i in range(2, n + 1):
            stairs[i] = stairs[i - 1] + stairs[i - 2]

        return stairs[n]
