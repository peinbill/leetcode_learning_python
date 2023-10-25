# -*- encoding: utf-8 -*-
"""
@File    : Solution11.py
@Time    : 2023/9/14 9:15 上午
@Author  : huangjinyu
@Desc   : 
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """ 基于双指针的方法进行

        @param height:
        @return:
        """
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans











