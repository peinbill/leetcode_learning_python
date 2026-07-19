#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/19 00:17
# @Author      : Jim
# @File        : Solution509.py
# @Software    : PyCharm
# @Description :
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)