#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/4 00:55
# @Author      : Jim
# @File        : Solution55.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_len = nums[0]

        for i in range(len(nums)):
            if i <= max_len:
                max_len = max(i + nums[i], max_len)

        return max_len >= len(nums) - 1