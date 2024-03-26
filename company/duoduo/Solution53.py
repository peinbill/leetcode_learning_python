#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/13 22:14
# @Author      : Jim
# @File        : Solution53.py
# @Software    : PyCharm
# @Description :

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_result = nums.copy()
        for i in range(1, len(nums)):
            nums_result[i] = max(nums_result[i - 1] + nums[i], nums[i])

        return max(nums_result)