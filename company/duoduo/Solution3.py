#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/13 21:41
# @Author      : Jim
# @File        : Solution3.py
# @Software    : PyCharm
# @Description : 滑动窗格的应用

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def boolean_shrink(window):
            for k, v in window.items():
                if v > 1:
                    return True
            return False

        if len(s) == 0:
            return 0

        max_len = 1
        left, right = 0, 0
        window = {}
        while right < len(s):
            ch = s[right]
            if ch in window:
                window[ch] = window[ch] + 1
            else:
                window[ch] = 1

            while boolean_shrink(window):
                d = s[left]
                window[d] = window[d] - 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len