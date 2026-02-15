#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/13 22:21
# @Author      : Jim
# @File        : Solution120.py
# @Software    : PyCharm
# @Description :
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle_new = [[float("inf") for j in i]for i in triangle]

        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    triangle_new[i][j] = triangle[i][j]
                else:
                    if j == 0:
                        triangle_new[i][j] = triangle_new[i-1][j]+triangle[i][j]
                    else:
                        triangle_new[i][j] = min(triangle_new[i-1][j-1],triangle_new[i-1][j])+triangle[i][j]



        return min(triangle_new[-1])
