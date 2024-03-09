#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 01:12
# @Author      : Jim
# @File        : Solution62.py
# @Software    : PyCharm
# @Description :


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for i in range(m)] for j in range(n)]

        for i in range(len(matrix[0])):
            matrix[0][i] = 1

        for i in range(len(matrix)):
            matrix[i][0] = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[-1][-1]

