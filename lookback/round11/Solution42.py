#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/4 00:58
# @Author      : Jim
# @File        : Solution42.py
# @Software    : PyCharm
# @Description :


# https://leetcode.cn/problems/trapping-rain-water/solutions/3986317/dan-diao-zhan-jie-fa-python-by-stupefied-nbcs/?envType=problem-list-v2&envId=2cktkvj

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans
