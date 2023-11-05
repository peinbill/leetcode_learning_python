# -*- encoding: utf-8 -*-
"""
@File    : Solution34.py
@Time    : 2023/10/30 10:46 下午
@Author  : huangjinyu
@Desc   : 基于二分查找的应用
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        left_index = -1
        right_index = -1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            left_index = left
        elif nums[right] == target:
            left_index = right

        if left_index == -1:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if nums[right] == target:
            right_index = right
        else:
            right_index = left

        return [left_index, right_index]
