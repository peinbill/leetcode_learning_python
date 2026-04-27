#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/27 23:18
# @Author      : Jim
# @File        : Solution415.py
# @Software    : PyCharm
# @Description :


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 存储最终结果（字符串形式）
        res = ""

        # i：num1 的指针，从**末尾**开始
        # j：num2 的指针，从**末尾**开始
        # carry：进位，初始为 0
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        # 循环条件：两个数字只要有一个没加完，或者还有进位，就继续
        while i >= 0 or j >= 0:
            # 取 num1 当前位的数字，如果 i 已经越界（数字加完了），就取 0
            n1 = int(num1[i]) if i >= 0 else 0
            # 取 num2 当前位的数字，如果 j 已经越界，就取 0
            n2 = int(num2[j]) if j >= 0 else 0

            # 当前位的总和 = 数字1 + 数字2 + 进位
            tmp = n1 + n2 + carry

            # 新的进位 = 总和 // 10（只保留十位）
            carry = tmp // 10
            # 当前位结果 = 总和 % 10（只保留个位），**往前拼接**到结果前面
            res = str(tmp % 10) + res

            # 两个指针都向左移动一位
            i, j = i - 1, j - 1

        # 最后如果还有进位，要在最前面补 1，否则直接返回结果
        return "1" + res if carry else res