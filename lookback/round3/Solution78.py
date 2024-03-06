#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/14 10:41
# @Author      : Jim
# @File        : Solution78.py
# @Software    : PyCharm
# @Description : 算法思维-回溯法
# 本质还是背公式
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
