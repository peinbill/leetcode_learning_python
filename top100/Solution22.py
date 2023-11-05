# -*- encoding: utf-8 -*-
"""
@File    : Solution22.py
@Time    : 2023/10/8 8:55 上午
@Author  : huangjinyu
@Desc   :
可以依照这个思路来进行逐步迭代
https://leetcode.cn/problems/generate-parentheses/solutions/597236/sui-ran-bu-shi-zui-xiu-de-dan-zhi-shao-n-0yt3/

"""

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

