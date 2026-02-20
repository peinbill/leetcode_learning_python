#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/18 23:35
# @Author      : Jim
# @File        : Solution912.py
# @Software    : PyCharm
# @Description :
from random import randint
from typing import List

from duckdb.experimental.spark.sql.functions import right


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums, low, high):
            if low>= high:
                return
            def partition(low, high):
                pirot = randint(low, high)
                nums[pirot],nums[high] = nums[high],nums[pirot]
                p = nums[high]

                i = low
                for j in range(low, high):
                    if nums[j] < p:
                        nums[j], nums[i] = nums[i], nums[j]
                        i = i + 1

                nums[i],nums[high] = nums[high],nums[i]

                return i

            index = partition(low, high)
            quicksort(nums, low, index - 1)
            quicksort(nums, index, high)

        quicksort(nums,0,len(nums)-1)
        return nums
