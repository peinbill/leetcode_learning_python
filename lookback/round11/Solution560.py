#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/4 01:23
# @Author      : Jim
# @File        : Solution560.py
# @Software    : PyCharm
# @Description :
from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        cnt = defaultdict(int)
        ans = 0
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans