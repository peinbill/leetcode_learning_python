#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/13 22:27
# @Author      : Jim
# @File        : Solution70.py
# @Software    : PyCharm
# @Description :

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2
        n_list = [0 for i in range(n)]

        n_list[0] = 1
        n_list[1] = 2

        for i in range(2,n):
            n_list[i] = n_list[i-1]+n_list[i-2]

        return n_list[n-1]