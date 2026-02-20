#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/20 12:29
# @Author      : Jim
# @File        : Solution78.py
# @Software    : PyCharm
# @Description : 核心还是在画图
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        track = []

        def bracktrack(tmp_list, start):
            result.append(tmp_list[:])
            for i in range(start, len(nums)):
                tmp_list.append(nums[i])
                bracktrack(tmp_list, i + 1)
                tmp_list.pop()

        bracktrack(track, 0)
        return result