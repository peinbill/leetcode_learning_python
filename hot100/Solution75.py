#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/4 01:05
# @Author      : Jim
# @File        : Solution75.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 分别指向0，1，2区域
        low, mid, high = 0, 0, len(nums) - 1
        # mid是活动指针
        while mid <= high:
            if nums[mid] == 0:  # 说明要交换到0区
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # 正好
                mid += 1
            else:  # 否则交换到2区
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
