#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 21:50
# @Author      : Jim
# @File        : Solution43.py
# @Software    : PyCharm
# @Description :
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 特判：任意一个数为0，结果直接是0
        if num1 == "0" or num2 == "0":
            return "0"

        # 最终乘积结果，初始为"0"
        ans = "0"
        # 获取两个数字字符串的长度
        m, n = len(num1), len(num2)

        # 遍历 num2 每一位，从低位到高位（倒序）
        for i in range(n - 1, -1, -1):
            # 进位变量
            add = 0
            # 取出 num2 当前位的数字
            y = int(num2[i])
            # 低位补0：第i位相乘，末尾需要补 (n-i-1) 个0
            curr = ["0"] * (n - i - 1)

            # 遍历 num1 每一位，从低位到高位（倒序）
            for j in range(m - 1, -1, -1):
                # 计算当前位乘积 + 上一轮进位
                product = int(num1[j]) * y + add
                # 取余数为当前位结果
                curr.append(str(product % 10))
                # 更新进位
                add = product // 10

            # 遍历结束，若还有剩余进位，追加到末尾
            if add > 0:
                curr.append(str(add))

            # 反转列表，转为正常顺序的数字字符串
            curr = "".join(curr[::-1])
            # 将当前轮相乘结果，累加到总结果
            ans = self.addStrings(ans, curr)

        return ans

    # 字符串高精度加法
    def addStrings(self, num1: str, num2: str) -> str:
        # 双指针分别指向两个字符串末尾（最低位）
        i, j = len(num1) - 1, len(num2) - 1
        # 进位标记
        add = 0
        # 存储加法结果字符
        ans = list()

        # 只要还有位数未遍历 或 存在进位，继续循环
        while i >= 0 or j >= 0 or add != 0:
            # 指针越界则当前位补0
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            # 同位相加 + 进位
            result = x + y + add
            # 保存当前个位
            ans.append(str(result % 10))
            # 计算新进位
            add = result // 10
            # 指针左移
            i -= 1
            j -= 1

        # 结果反转，拼接为正常数字字符串
        return "".join(ans[::-1])