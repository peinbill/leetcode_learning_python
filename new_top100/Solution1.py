#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/20 12:39
# @Author      : Jim
# @File        : Solution1.py
# @Software    : PyCharm
# @Description :
from typing import List

class Solution:
    class Solution:

        # def twoSum(self, nums: List[int], target: int) -> List[int]:
        #     hashtable = dict()
        #     for i, num in enumerate(nums):
        #         if target - num in hashtable:
        #             return [hashtable[target - num], i]
        #         hashtable[nums[i]] = i
        #     return []
        # def twoSum(self, nums: List[int], target: int) -> List[int]:
        #     for i in range(len(nums)):
        #         for j in range(i+1,len(nums)):
        #             if nums[j] == target - nums[i]:
        #                 return [i,j]

        def twoSum(self, nums: List[int], target: int) -> List[int]:
            num_dict = {}

            for i, j in enumerate(nums):
                num_dict[j] = i

            for i, j in enumerate(nums):
                result = target - j
                if result in num_dict and num_dict[result] != i:
                    return [i, num_dict[result]]