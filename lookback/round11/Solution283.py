#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/4 08:24
# @Author      : Jim
# @File        : Solution283.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i0 = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1
