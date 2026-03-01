#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/3/1 19:56
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
                if len(stack)==0:
                    return False
                tmp = stack.pop()
                if tmp != "{":
                    return False
            if i == ")":
                if len(stack)==0:
                    return False
                tmp = stack.pop()
                if tmp != "(":
                    return False
            if i == "]":
                if len(stack)==0:
                    return False
                tmp = stack.pop()
                if tmp != "[":
                    return False
        return len(stack) == 0