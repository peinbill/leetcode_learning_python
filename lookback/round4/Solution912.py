#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/2/25 10:57
# @Author      : Jim
# @File        : Solution912.py
# @Software    : PyCharm
# @Description :

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_list, right_list):
            C = []
            i, j = 0, 0
            while i < len(left_list) and j < len(right_list):
                if left_list[i] < right_list[j]:
                    C.append(left_list[i])
                    i += 1
                else:
                    C.append(right_list[j])
                    j += 1

            while i < len(left_list):
                C.append(left_list[i])
                i += 1

            while j < right_list:
                C.append(right_list[j])
                j += 1

            return C

        def mergeSort(nums):
            n = len(nums)
            if n < 2:
                return nums

            left_list = mergeSort(nums[:n // 2])
            right_list = mergeSort(nums[n // 2:])
            return merge(left_list, right_list)

        rtn_nums = mergeSort(nums, 0, len(nums) - 1)

        return rtn_nums
