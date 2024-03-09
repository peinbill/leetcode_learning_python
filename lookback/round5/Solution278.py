#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 00:44
# @Author      : Jim
# @File        : Solution278.py
# @Software    : PyCharm
# @Description : 二分查找
# The isBadVersion API is already defined for you.

def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n

        while left+1<right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid

            else:
                left = mid

        if isBadVersion(left):
            return left
        else:
            return right


