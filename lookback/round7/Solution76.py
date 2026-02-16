#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/16 13:45
# @Author      : Jim
# @File        : Solution76.py
# @Software    : PyCharm
# @Description :
from collections import Counter
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        cnt = Counter(t)
        need = len(t)
        n = len(s)
        start,end = 0,-1
        min_len = n+1
        left,right = 0,0

        for right in range(n):
            ch = s[right]
            if ch in cnt:
                if cnt[ch] >0:
                    need -=1
                cnt[ch] -= 1
            while need == 0:
                if right-left+1 < min_len:
                    min_len = right-left+1
                    start,end = left,right
                ch = s[left]
                if ch in cnt:
                    if cnt[ch] >= 0:
                        need +=1
                    cnt[ch] += 1
                left+=1
        return s[start:end+1]