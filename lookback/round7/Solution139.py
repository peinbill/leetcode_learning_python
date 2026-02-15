#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/15 21:15
# @Author      : Jim
# @File        : Solution139.py
# @Software    : PyCharm
# @Description : 双序列大零钱问题
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]
