#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/3 23:26
# @Author      : Jim
# @File        : Solution01.py
# @Software    : PyCharm
# @Description :

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []