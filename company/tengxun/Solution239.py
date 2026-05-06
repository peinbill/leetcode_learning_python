#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 19:56
# @Author      : Jim
# @File        : Solution239.py
# @Software    : PyCharm
# @Description :
from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 双向队列：存储的是 **下标**
        # 维护规则：队列中下标对应的元素 **从大到小**
        q = collections.deque()

        # 第一步：先处理第一个窗口 [0 ~ k-1]
        for i in range(k):
            # 维护单调递减：如果当前数 >= 队列尾部下标对应的数
            # 说明尾部数永远不可能成为最大值，直接弹出
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            # 将当前下标加入队列尾部
            q.append(i)

        # 第一个窗口的最大值就是队列头部下标对应的值
        ans = [nums[q[0]]]

        # 第二步：滑动窗口，从 k 开始到末尾
        for i in range(k, n):
            # 同样维护单调递减：移除所有比当前数小的尾部元素
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

            # 检查队头：如果下标已经 **滑出窗口**，移除
            # 窗口范围：[i-k+1 ... i]，所以 <= i-k 就是过期
            while q[0] <= i - k:
                q.popleft()

            # 此时队头就是当前窗口最大值
            ans.append(nums[q[0]])

        return ans