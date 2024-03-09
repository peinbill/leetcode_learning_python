#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 01:47
# @Author      : Jim
# @File        : Solution509.py
# @Software    : PyCharm
# @Description : 说是递归，但是动态规划更好


class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n

        dp = [0 for i in range(n+1)]

        dp[0] = 0
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[-1]