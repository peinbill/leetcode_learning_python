#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/12/30 23:19
# @Author      : Jim
# @File        : Solution78.py
# @Software    : PyCharm
# @Description :回溯法，核心在于我们通过保证元素之间的相对顺序不变来防止出现重复的子集。
#（其实，这道题就比较适合用于作为死记硬背回溯算法的题目）
from typing import List


class Solution:

    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    # 主函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res

    # 回溯算法核心函数，遍历子集问题的回溯树
    def backtrack(self, nums: List[int], start: int) -> None:
        # 前序位置，每个节点的值都是一个子集
        self.res.append(list(self.track))

        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i])
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(nums, i + 1)
            # 撤销选择
            self.track.pop()