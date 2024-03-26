#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/23 16:21
# @Author      : Jim
# @File        : Solution200.py
# @Software    : PyCharm
# @Description : 岛屿数量

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0

        def DFS(i, j):
            grid[i][j] = "0"
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                    DFS(tmp_i, tmp_j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    DFS(i, j)
                    ans += 1
        return ans

