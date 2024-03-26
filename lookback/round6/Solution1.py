#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/15 22:43
# @Author      : Jim
# @File        : Solution1.py
# @Software    : PyCharm
# @Description : 基于two_sum 改进

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for index, i in enumerate(nums):
            nums_dict[i] = index

        for i in nums:
            result = target - i
            if result in nums_dict:
                return [nums[i], nums[result]]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
