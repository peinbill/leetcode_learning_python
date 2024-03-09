#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 00:02
# @Author      : Jim
# @File        : Solution496.py
# @Software    : PyCharm
# @Description : 单调栈+链表
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        n = len(nums2)
        res = [-1 for i in nums2]

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(nums2[i])

        index_dict = dict()
        for index, i in enumerate(nums2):
            index_dict[i] = index

        rtn = []
        for i in nums1:
            index = index_dict[i]
            rtn.append(res[index])
        return rtn