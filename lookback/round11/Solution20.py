#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/4 08:25
# @Author      : Jim
# @File        : Solution20.py
# @Software    : PyCharm
# @Description :
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            if i == "}":
                tmp = stack.pop()
                if tmp != "{":
                    return False
            if i == ")":
                tmp = stack.pop()
                if tmp != "(":
                    return False
            if i == "]":
                tmp = stack.pop()
                if tmp != "[":
                    return False
        return len(stack) == 0