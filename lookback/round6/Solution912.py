#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/16 07:31
# @Author      : Jim
# @File        : Solution912.py
# @Software    : PyCharm
# @Description : 手撕快速排序

import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, l, r):
        def find_pirot(num,l,r):
            p = random.randint(l,r)
            p_val = num[p]

            num[p],num[r] = nums[r],num[p]

            i ,j = l,l

            for i in range(l,r):
                if num[i]<p_val:
                    num[i],num[j] = nums[j],num[i]
                    j+=1

            num[j],num[r] = num[r],num[j]

            return j


        if l<r:
            pirot = find_pirot(nums,l,r)
            self.quickSort(nums,l,pirot)
            self.quickSort(nums,pirot+1,r)

        return nums