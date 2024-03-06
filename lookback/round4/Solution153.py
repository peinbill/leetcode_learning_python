#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/2/25 10:57
# @Author      : Jim
# @File        : Solution153.py
# @Software    : PyCharm
# @Description :


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left+1 < right:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid

        if nums[left] > nums[right]:
            return nums[right]
        else:
            return nums[left]