#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/1 20:06
# @Author      : Jim
# @File        : Solution153.py
# @Software    : PyCharm
# @Description : 基础算法-二分查找

# 部分有序，其实本质上就是要找到循转的点

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid

        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]