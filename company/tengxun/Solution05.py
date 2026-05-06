#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/5 22:11
# @Author      : Jim
# @File        : Solution05.py
# @Software    : PyCharm
# @Description :
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            # 左右指针扩散
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 跳出时不满足，截取合法回文
            return s[left + 1:right]

        res = ""
        for i in range(len(s)):
            # 奇数回文
            odd = expand(i, i)
            # 偶数回文
            even = expand(i, i + 1)
            # 更新最长
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res