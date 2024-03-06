#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/8 23:08
# @Author      : Jim
# @File        : Solution200.py
# @Software    : PyCharm
# @Description : 数据结构——栈和队列
# 岛屿问题

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        land_num = 0
        row_len = len(grid)
        col_len = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= row_len:
                return
            if j < 0 or j >= col_len:
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    land_num += 1
                    dfs(i, j)
        return land_num