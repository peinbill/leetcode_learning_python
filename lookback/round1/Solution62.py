#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/12/17 21:52
# @Author      : Jim
# @File        : Solution62.py
# @Software    : PyCharm
# @Description : 直接经典的动态规划算法

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            matrix[i][0] = 1

        for i in range(n):
            matrix[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]

        return matrix[m-1][n-1]