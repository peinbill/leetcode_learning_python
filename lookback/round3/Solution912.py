#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/8 23:50
# @Author      : Jim
# @File        : Solution912.py
# @Software    : PyCharm
# @Description :

from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if self.boolean_sort(nums):
            return nums
        return self.quick_sort(nums)

    def quick_sort(self, nums: List[int]) -> List[int]:
        """
            使用快速排序
            这一题很老6，快排是过不了的
        """

        def quickSort(nums, l, r):
            if l >= r:
                return

            pivort = partition(nums, l, r)

            quickSort(nums, l, pivort - 1)
            quickSort(nums, pivort, r)

        def partition(nums, l, r):
            pirot = random.randint(l, r)
            # 先随机选择数据，再跟最后一个数进行交换
            nums[pirot], nums[r] = nums[r], nums[pirot]
            p = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= p:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]

            return i

        quickSort(nums, 0, len(nums) - 1)

        return nums