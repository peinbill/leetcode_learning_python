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
        if len(tokens)==0:
            return 0

        symbols = ["+","-","*","/"]

        number_stack = list()

        for i in tokens:
            if i in symbols:
                number1 = number_stack.pop()
                number2 = number_stack.pop()
                if i == "+":
                    number = number1+number2
                if i == "-":
                    number = number2-number1
                if i == "*":
                    number = number1*number2
                if i == '/':
                    number = int(number2/number1)
                number_stack.append(i)
            else:
                number_stack.append(int(i))


        return number_stack.pop()

if __name__ == "__main__":
    solution = Solution()
    solution.evalRPN(["18"])