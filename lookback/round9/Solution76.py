#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/8 08:01
# @Author      : Jim
# @File        : Solution76.py
# @Software    : PyCharm
# @Description :
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_size = len(s)
        min_sub_string = ""
        left, right = 0, 0

        cnt = Counter(t)
        need = len(t)

        while right < len(s):
            ch = s[right]
            if ch in cnt:
                if cnt.get(ch) > 0:
                    need -= 1
                cnt[ch] -= 1

            while need == 0:
                if right - left + 1 <= window_size:
                    window_size = right - left + 1
                    min_sub_string = s[left:right + 1]

                ch = s[left]

                if ch in cnt:
                    cnt[ch] += 1
                    if cnt[ch] > 0:
                        need += 1

                left += 1

            right += 1

        return min_sub_string