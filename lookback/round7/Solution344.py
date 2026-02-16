#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/16 10:32
# @Author      : Jim
# @File        : Solution344.py
# @Software    : PyCharm
# @Description :


from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:

        def revert(l,r):
            if l>= r:
                return
            s[l],s[r] = s[r],s[l]
            revert(l+1,r-1)
        revert(0,len(s)-1)