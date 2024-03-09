#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 00:49
# @Author      : Jim
# @File        : Solution912.py
# @Software    : PyCharm
# @Description : 快速排序

import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, l, r):

        def find_pirot(nums, l, r):
            p = random.randint(l, r)

            nums[p], nums[r] = nums[r], nums[p]
            pirot = nums[r]

            i, j = l,l
            while i < r:
                if nums[i] <= pirot:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                i+=1

            nums[j], nums[r] = nums[r], nums[j]
            return j

        if l >= r:
            return
        pirot = find_pirot(nums,l,r)
        self.quickSort(nums, l, pirot-1)
        self.quickSort(nums, pirot, r)
        return nums
