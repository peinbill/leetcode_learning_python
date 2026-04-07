#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/7 23:33
# @Author      : Jim
# @File        : Solution912.py
# @Software    : PyCharm
# @Description :
from random import randint
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partion(nums,start,end):
            p = randint(start,end)
            nums[end],nums[p] = nums[p],nums[end]
            p_val = nums[end]
            i = start
            for j in range(start,end):
                if nums[j]<=p_val:
                    nums[j],nums[i] = nums[i],nums[j]
                    i+=1
            nums[i],nums[end] = nums[end],nums[i]
            return i
        def quick_sort(nums,start,end):
            if start>=end:
                return
            pivot = partion(nums,start,end)
            quick_sort(nums,start,pivot-1)
            quick_sort(nums,pivot+1,end)
        quick_sort(nums,0,len(nums)-1)
        return nums