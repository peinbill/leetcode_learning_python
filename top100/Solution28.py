# -*- encoding: utf-8 -*-
"""
@File    : Solution26.py
@Time    : 2023/10/26 11:13 下午
@Author  : huangjinyu
@Desc   : 
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        need_len = len(needle)
        for i in range(len(haystack)-need_len+1):
            match = haystack[i:i+need_len]
            if match == needle:
                return i

        return -1
