#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 21:57
# @Author      : Jim
# @File        : Solution72.py
# @Software    : PyCharm
# @Description :
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # dp[i][j]：word1前i个字符 转为 word2前j个字符 的最小编辑距离
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化边界：
        # word1为空，只能不断插入word2字符
        for j in range(1, n + 1):
            dp[0][j] = j
        # word2为空，只能不断删除word1字符
        for i in range(1, m + 1):
            dp[i][0] = i

        # 遍历所有子问题
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 当前字符相等：无需操作，直接继承前一位结果
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 三者取最小值 + 1（当前一次操作）
                    # 1.替换：dp[i-1][j-1] + 1
                    # 2.删除word1：dp[i-1][j] + 1
                    # 3.插入word1(等价删除word2)：dp[i][j-1] + 1
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        # 完整字符串的最小编辑距离
        return dp[m][n]