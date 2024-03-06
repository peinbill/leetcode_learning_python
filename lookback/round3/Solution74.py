#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/9 22:35
# @Author      : Jim
# @File        : Solution74.py
# @Software    : PyCharm
# @Description : 基础算法—二分查找

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        full_list = []
        for i in matrix:
            full_list.extend(i)

        return self.binary_search(full_list, target)

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False