#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/4 08:21
# @Author      : Jim
# @File        : Solution22.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0: return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left: return
            if len(paths) == n * 2:  # 因为括号都是成对出现的
                res.append(paths)
                return

            dfs(paths + '(', left + 1, right)  # 生成一个就加一个
            dfs(paths + ')', left, right + 1)

        dfs('', 0, 0)
        return res
