#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/18 18:38
# @Author      : Jim
# @File        : Solution200.py
# @Software    : PyCharm
# @Description :

from typing import List

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        total_land = 0
        m = len(grid)
        n = len(grid[0])

        visited_place = [[False for j in range(n)] for i in range(m)]

        def dfs(i, j):
            if i < 0 or i > m - 1:
                return
            if j < 0 or j > n - 1:
                return

            if visited_place[i][j] == True:
                return

            if grid[i][j] == 0:
                visited_place[i][j] = True
                return

            else:
                total_land += 1
                visited_place[i][j] = True

                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                dfs(i, j)

        return total_land