#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/16 00:53
# @Author      : Jim
# @File        : Solution912.py
# @Software    : PyCharm
# @Description :

import random
from typing import List

class Solution:
    def sortArray3(self, nums: List[int]) -> List[int]:
        """
        堆排序
        @param nums:
        @return:
        """
    def sortArray2(self, nums: List[int]) -> List[int]:
        """
        归并排序
        @param nums:
        @return:
        """

        if not nums:
            return nums
        def merge(A,B):
            c = []
            i,j = 0,0
            while i < len(A) and j < len(B):
                if A[i] < B[j]:
                    c.append(A[i])
                    i += 1
                else:
                    c.append(B[j])
                    j += 1

            while i < len(A):
                c.append(A[i])
                i += 1

            while j < len(B):
                c.append(B[j])

                j+=1
            return c
        def mergeSort(nums):
            if len(nums) < 2:
                return nums
            left = mergeSort(nums[:len(nums) // 2])
            right = mergeSort(nums[len(nums) // 2:])
            return merge(left, right)
        nums = mergeSort(nums)
        return nums



    def sortArray(self, nums: List[int]) -> List[int]:
        """
        快速排序
        @param nums:
        @return:
        """
        if len(nums) == 0:
            return nums

        def partion(l, r):
            pirot = random.randint(l, r)
            nums[r], nums[pirot] = nums[pirot], nums[r]
            p = nums[r]

            i = l
            for j in range(l, r):
                if nums[j] <= p:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def quick_sort(l, r):
            if l >= r:
                return
            pirot = partion(l, r)
            quick_sort(l, pirot - 1)
            quick_sort(pirot, r)

        quick_sort(0, len(nums) - 1)
        return nums

