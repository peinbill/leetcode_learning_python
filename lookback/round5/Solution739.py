#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 00:39
# @Author      : Jim
# @File        : Solution739.py
# @Software    : PyCharm
# @Description : 单调栈

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans