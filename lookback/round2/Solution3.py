#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/1 22:09
# @Author      : Jim
# @File        : Solution3.py
# @Software    : PyCharm
# @Description : 算法思想-滑动窗格思维

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def has_duplicate(_dict):
            for i, v in _dict.items():
                if v > 1:
                    return True
            return False

        max_len = 0
        window = {}
        left, right = 0, 0
        while right < len(s):
            c = s[right]

            if c not in window:
                window[c] = 1
            else:
                window[c] += 1

            right += 1

            while window[c] > 1:
                d = s[left]
                window[d] -= 1
                left += 1

            max_len = max(max_len, right - left)
        return max_len

