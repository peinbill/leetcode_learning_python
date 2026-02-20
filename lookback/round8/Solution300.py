#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/19 00:00
# @Author      : Jim
# @File        : Solution300.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1 for i in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)