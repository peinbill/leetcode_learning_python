#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/3/7 08:01
# @Author      : Jim
# @File        : Solution35.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[right] < target:
            return right + 1
        if nums[left] < target:
            return right

        return left