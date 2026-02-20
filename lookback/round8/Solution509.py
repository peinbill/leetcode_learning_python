#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/19 00:06
# @Author      : Jim
# @File        : Solution509.py
# @Software    : PyCharm
# @Description :
class Solution:

    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    def fib2(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]