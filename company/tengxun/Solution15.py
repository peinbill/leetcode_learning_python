#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 20:34
# @Author      : Jim
# @File        : Solution15.py
# @Software    : PyCharm
# @Description :
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 数组排序，为双指针 + 去重做准备
        nums.sort()
        # 存储最终三元组结果
        result = list()

        # 遍历固定第一个数 nums[i]
        for i in range(len(nums)):
            # 跳过重复的第一个数，避免产出重复三元组
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            # 在 i 右侧区间，寻找两数之和 = -nums[i]
            # 目标：nums[i] + a + b = 0
            rtn = self.twoSum(nums, i + 1, len(nums) - 1, 0 - nums[i])

            # 如果找到符合条件的二元组，拼接成三元组存入结果
            if rtn:
                for rtn_1, rtn_2 in rtn:
                    tmp_result = [nums[i], rtn_1, rtn_2]
                    result.append(tmp_result)

        return result

    def twoSum(self, nums, start, end, target):
        # 集合：用来对二元组去重
        result_set = set()
        # 存放当前合法的两数组合
        result = []

        # 双指针相向遍历
        while start < end:
            cur_sum = nums[start] + nums[end]
            if cur_sum == target:
                # 组合未出现过，才加入结果
                if (nums[start], nums[end]) not in result_set:
                    result.append((nums[start], nums[end]))
                    result_set.add((nums[start], nums[end]))
                # 左右指针同时收缩，继续查找
                start += 1
                end -= 1
            elif cur_sum > target:
                # 和偏大，右指针左移，减小总和
                end -= 1
            else:
                # 和偏小，左指针右移，增大总和
                start += 1

        # 返回当前区间所有和为 target 的不重复二元组
        return result