#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/23 16:00
# @Author      : Jim
# @File        : Solution20.py
# @Software    : PyCharm
# @Description :

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in set(["(","{","["]):
                stack.append(i)
            else:
                try:
                    top = stack[-1]
                except:
                    return False
                if i =="]" and top == "[":
                    stack.pop()
                elif i == "}" and top == "{":
                    stack.pop()
                elif i==")" and top == "(":
                    stack.pop()

                else:
                    return False


        return len(stack)==0