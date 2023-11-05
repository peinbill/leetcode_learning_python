# -*- encoding: utf-8 -*-
"""
@File    : Solution26.py
@Time    : 2023/10/26 11:13 下午
@Author  : huangjinyu
@Desc   : 
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


