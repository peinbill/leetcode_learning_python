#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution150.py
@time: 2022/4/30 8:05
@Describe:
"""
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens)==0:
            return 0

        for token in tokens:
            if token == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                token = num1+num2
            elif token == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                token = num2-num1
            elif token == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                token = num2*num1
            elif token == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                token = num2/num1
            stack.append(token)

        return int(stack[0])

if __name__ == "__main__":
    solution = Solution()
    solution.evalRPN(["18"])