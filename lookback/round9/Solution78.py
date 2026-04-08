#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/8 08:17
# @Author      : Jim
# @File        : Solution78.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp_result = []

        def brack(set_len, index):
            if len(tmp_result) == set_len:
                result.append(tmp_result.copy())
                return

            for i in range(index, len(nums)):
                tmp_result.append(nums[i])
                brack(set_len, i + 1)
                tmp_result.pop()

        for i in range(len(nums) + 1):
            brack(i, 0)
        return result