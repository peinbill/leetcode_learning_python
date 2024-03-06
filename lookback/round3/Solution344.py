#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/13 12:22
# @Author      : Jim
# @File        : Solution344.py
# @Software    : PyCharm
# @Description : 算法思想-递归

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if s == None:
            return s

        def rever(str, i, j):
            if i >= j:
                return str
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
            rever(str, i, j)

        rever(s, 0, len(s) - 1)