#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/18 18:20
# @Author      : Jim
# @File        : Solution155.py
# @Software    : PyCharm
# @Description :
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