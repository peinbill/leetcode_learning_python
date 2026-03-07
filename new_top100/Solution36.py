#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/3/7 08:21
# @Author      : Jim
# @File        : Solution36.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        row = [[] * 9 for _ in range(9)]
        col = [[] * 9 for _ in range(9)]
        nine = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(n):
            for j in range(m):
                tmp = board[i][j]
                if not tmp.isdigit():
                    continue
                if tmp in row[i]:
                    return False
                if tmp in col[j]:
                    return False
                if tmp in nine[i//3][j//3]:
                    return False
                row[i].append(tmp)
                col[j].append(tmp)
                nine[i//3][j//3].append(tmp)
        return True