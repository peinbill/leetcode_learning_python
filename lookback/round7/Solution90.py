#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/16 11:25
# @Author      : Jim
# @File        : Solution90.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def reformat_intlist2str(self, int_list: List[int]):
        if len(int_list) == 0:
            return ""
        str_list = [str(i) for i in int_list]

        return ",".join(str_list)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        track = []
        nums = sorted(nums)
        set_result = set()

        def bracktrack(tmp_list, start):

            if self.reformat_intlist2str(tmp_list[:]) not in set_result:
                result.append(tmp_list[:])
                set_result.add(self.reformat_intlist2str(tmp_list[:]))
            for i in range(start, len(nums)):
                tmp_list.append(nums[i])
                bracktrack(tmp_list, i + 1)
                tmp_list.pop()

        bracktrack(track, 0)
        return result