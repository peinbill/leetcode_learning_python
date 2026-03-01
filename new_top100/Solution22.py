#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/3/1 23:38
# @Author      : Jim
# @File        : Solution22.py
# @Software    : PyCharm
# @Description :
from typing import List
class Solution:
    def isValid(self, s: List[str]) -> bool:
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            if i == ")":
                if len(stack)==0:
                    return False
                tmp = stack.pop()
                if tmp != "(":
                    return False
        return len(stack) == 0

    def generateParenthesis(self, n: int) -> List[str]:
        def validate_tmp(str_list):
            if len(str_list) == 0:
                return True
            tmp_left = 0
            tmp_right = 0
            for i in str_list:
                if i == "(":
                    tmp_left += 1
                if i == ")":
                    tmp_right+=1
            if tmp_left>n:
                return False
            if tmp_right > n:
                return False
            if tmp_right>tmp_left:
                return False
            return True

        def brack_track(i):
            if i == 2*n:
                if validate_tmp(collection):
                    collections.append("".join(collection))
                return
            if validate_tmp(collection) is False:
                return
            for j in ["(",")"]:
                collection.append(j)
                brack_track(i+1)
                collection.pop()

        collection = []
        collections = []
        brack_track(0)
        return collections