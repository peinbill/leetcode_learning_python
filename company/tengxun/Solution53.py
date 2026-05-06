#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 20:26
# @Author      : Jim
# @File        : Solution53.py
# @Software    : PyCharm
# @Description :
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current：以当前元素结尾的最大子数组和
        current = nums[0]
        # res：全局遍历到的最大子数组和
        res = nums[0]

        # 从第二个元素开始遍历
        for num in nums[1:]:
            # 核心抉择：
            # 1. 接上前面的子数组：current + num
            # 2. 抛弃前面，以当前数重新开始：num
            # 选二者较大值
            current = max(num, current + num)

            # 更新全局最大值
            res = max(res, current)

        return res