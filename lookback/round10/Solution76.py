#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/19 08:55
# @Author      : Jim
# @File        : Solution76.py
# @Software    : PyCharm
# @Description :
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # 初始化为空，代表暂无合法子串
        min_sub_string = ""
        cnt = Counter(t)
        need = len(t)
        left, right = 0, 0

        while right < len(s):
            ch = s[right]
            if ch in cnt:
                # 只有还需要该字符时，才消耗need
                if cnt[ch] > 0:
                    need -= 1
                cnt[ch] -= 1

            # 满足条件，收缩左边界
            while left <= right and need == 0:
                cur_len = right - left + 1
                # 两种情况更新：1.还没存过子串 2.当前窗口更小
                if min_sub_string == "" or cur_len < len(min_sub_string):
                    min_sub_string = s[left:right + 1]

                left_ch = s[left]
                if left_ch in cnt:
                    cnt[left_ch] += 1
                    # 恢复需求，need增加
                    if cnt[left_ch] > 0:
                        need += 1
                left += 1
            right += 1
        return min_sub_string