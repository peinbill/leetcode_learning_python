# -*- encoding: utf-8 -*-
"""
@File    : Solution36.py
@Time    : 2023/10/30 10:47 下午
@Author  : huangjinyu
@Desc   : 比较难想出这是一道动态规划调题目
初始以为是基于状态机完成
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)


        # 初始状态设置
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]



