#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/5 22:27
# @Author  : Jim
# @File    : Solution278.py
# @Software: PyCharm
# 使用二分查找模板3

def isBadVersion(n):
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left +1<right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        if isBadVersion(left):
            return left
        else:
            return right