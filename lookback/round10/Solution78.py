#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/19 09:09
# @Author      : Jim
# @File        : Solution78.py
# @Software    : PyCharm
# @Description :
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 保存最终所有子集结果
        res = []
        # 保存当前正在构建的路径（当前子集）
        path = []

        def backtrack(start: int):
            """
            回溯函数
            start：本轮从哪个下标开始选（保证不回头、不重复）
            """
            # 核心：子集问题 —— 所有节点都要收集
            # 只要进入递归，当前 path 就是一个合法子集
            res.append(path.copy())

            # 从 start 开始遍历，避免选到前面的数，产生重复子集
            for i in range(start, len(nums)):
                # 1. 选择：把当前数字加入路径
                path.append(nums[i])

                # 2. 递归：下一轮只能选 i+1 之后的数，保证升序不重复
                backtrack(i + 1)

                # 3. 回溯：撤销选择，恢复现场
                path.pop()

        # 从第0个位置开始选
        backtrack(0)
        return res