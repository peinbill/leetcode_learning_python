#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution84.py
@time: 2022/5/8 22:20
@Describe:
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """ 方法一：暴力破解法，但是会超时

        :param heights:
        :return:
        """
        size = len(heights)
        res = 0

        for i in range(size):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1

            right = i
            while right < size - 1 and heights[right + 1] >= cur_height:
                right += 1

            max_width = right - left + 1
            res = max(res, max_width * cur_height)
        return res

    def largestRectangleArea2(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                # 除了右边要比当前严格小，其实还蕴含了一个条件，那就是左边也要比当前高度严格小。
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res
#
# 作者：liweiwei1419
# 链接：https://leetcode.cn/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



