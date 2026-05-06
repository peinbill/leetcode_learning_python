#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 22:07
# @Author      : Jim
# @File        : Solution88.py
# @Software    : PyCharm
# @Description :
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        不要返回任何内容，原地修改 nums1
        """
        # p1：nums1 有效元素末尾下标
        p1 = m - 1
        # p2：nums2 末尾下标
        p2 = n - 1
        # cur：nums1 待填充位置（从最后往前）
        cur = m + n - 1

        # 倒序遍历，大数先放后面
        while p1 >= 0 and p2 >= 0:
            # 选更大的数放入当前位置
            if nums1[p1] > nums2[p2]:
                nums1[cur] = nums1[p1]
                p1 -= 1
            else:
                nums1[cur] = nums2[p2]
                p2 -= 1
            # 填充位置前移
            cur -= 1

        # 若 nums2 还有剩余元素，全部依次填入前面
        while p2 >= 0:
            nums1[cur] = nums2[p2]
            p2 -= 1
            cur -= 1