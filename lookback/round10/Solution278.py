#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/18 23:36
# @Author      : Jim
# @File        : Solution278.py
# @Software    : PyCharm
# @Description :
def isBadVersion(version: int) -> bool:
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
        return right