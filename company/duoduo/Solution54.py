#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/13 21:16
# @Author      : Jim
# @File        : Solution54.py
# @Software    : PyCharm
# @Description :

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ 1框带1框

        @param matrix:
        @return:
        """
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])

            # 这里可能没有回头路
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

        def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
            """
                转转转
            @param self:
            @param matrix:
            @return:
            """
            if not matrix: return []
            l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
            while True:
                for i in range(l, r + 1): res.append(matrix[t][i])  # left to right
                t += 1
                if t > b: break
                for i in range(t, b + 1): res.append(matrix[i][r])  # top to bottom
                r -= 1
                if l > r: break
                for i in range(r, l - 1, -1): res.append(matrix[b][i])  # right to left
                b -= 1
                if t > b: break
                for i in range(b, t - 1, -1): res.append(matrix[i][l])  # bottom to top
                l += 1
                if l > r: break
            return res

