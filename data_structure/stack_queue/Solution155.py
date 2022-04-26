#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution155.py
@time: 2022/4/26 22:54
@Describe:
"""

"""
        基于辅助栈
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value_list = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_value = self.min_value_list[-1]
        if val < self.min_value_list[-1]:
            min_value = val

        self.min_value_list.append(min_value)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()
        self.min_value_list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value_list[-1]