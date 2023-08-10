#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution200.py
@time: 2022/5/8 22:05
@Describe:
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m:
                return
            if j<0 or j>=n:
                return
            if grid[i][j] == "0":
                return

            if grid[i][j]=="1":
                grid[i][j] = "0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)

        return count