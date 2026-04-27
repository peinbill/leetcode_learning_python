#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/27 22:41
# @Author      : Jim
# @File        : Solution45.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for i in nums]

        dp[0] = 0
        for i in range(len(nums)):
            max_index = min(i+nums[i],len(nums)-1)
            for j in range(i,max_index+1):
                dp[j] = min(dp[i]+1,dp[j])
        return dp[-1]


    def jump2(self, nums: List[int]) -> int:
        end = 0
        farest = 0
        step = 0
        for i in range(len(nums)-1):
            farest = max(farest,i+nums[i])
            if i>= end:
                end = farest
                step += 1

        return step