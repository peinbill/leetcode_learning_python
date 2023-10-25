# -*- encoding: utf-8 -*-
"""
@File    : Solution1.py
@Time    : 2023/8/16 6:35 上午
@Author  : huangjinyu
@Desc   : 
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first_val = nums[i]
            for j in range(i + 1, len(nums)):
                second_val = nums[j]
                if first_val + second_val == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
