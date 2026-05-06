#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 21:32
# @Author      : Jim
# @File        : Solution27.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 0
        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow