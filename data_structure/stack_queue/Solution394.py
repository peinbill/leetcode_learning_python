#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution394.py
@time: 2022/4/30 8:25
@Describe:
"""

class Solution:
    def decodeString(self, s: str) -> str:
        """ 两个栈，一个用来存数，一个用来存字符串

        :param s:
        :return:
        """

        stack_str = ['']
        stack_num = []

        num = 0
        for c in s:
            if c >= '0' and c <= '9':
                num = num * 10 + int(c)
            elif c == '[':
                stack_num.append(num)
                stack_str.append('')
                num = 0
            elif c == ']':
                cur_str = stack_str.pop()
                stack_str[-1] += cur_str * stack_num.pop()
            else:
                stack_str[-1] += c

        return stack_str[0]



