#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/27 23:15
# @Author      : Jim
# @File        : Solution300.py
# @Software    : PyCharm
# @Description :
from typing import List  # 类型提示需要（LeetCode已自动导入）


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 边界条件：如果数组为空，最长递增子序列长度为 0
        if not nums:
            return 0

        # dp[i] 表示：以 nums[i] 这个数字结尾的最长递增子序列的长度
        # 初始化：每个数字自己单独就是一个长度为 1 的子序列
        dp = []

        # 遍历数组中的每一个数字 nums[i]
        for i in range(len(nums)):
            # 初始时，每个位置的最长长度都是 1（只有自己）
            dp.append(1)

            # 遍历 i 前面所有的数字 nums[j]（j < i）
            for j in range(i):
                # 核心条件：如果当前数字 nums[i] 比前面的 nums[j] 大
                # 说明可以把 nums[i] 接在以 nums[j] 结尾的递增子序列后面
                if nums[i] > nums[j]:
                    # 更新 dp[i]：
                    # 要么保持原来的值，要么取 dp[j]+1（更长的子序列）
                    dp[i] = max(dp[i], dp[j] + 1)

        # dp 数组里的最大值，就是整个数组的最长递增子序列长度
        return max(dp)