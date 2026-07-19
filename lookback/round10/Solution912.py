#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/18 23:47
# @Author      : Jim
# @File        : Solution912.py
# @Software    : PyCharm
# @Description :
from random import randint
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums: List[int], l: int, r: int):
        # 递归终止：区间只有一个数或无元素，无需排序
        if l >= r:
            return

        # Lomuto分区函数，随机基准优化有序数组退化问题
        def partition(nums: List[int], l: int, r: int) -> int:
            # 随机选取基准下标，交换到右端
            p = randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            j = l  # j：小于基准区域的右边界
            # i遍历 [l, r-1] 所有元素
            for i in range(l, r):
                # 当前元素小于基准，划入小区间
                if nums[i] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            # 将基准值放到分割点j
            nums[j], nums[r] = nums[r], nums[j]
            return j

        # 获取分割下标
        pivot = partition(nums, l, r)
        # 递归排序左右两段，跳过pivot本身
        self.quickSort(nums, l, pivot - 1)
        self.quickSort(nums, pivot + 1, r)