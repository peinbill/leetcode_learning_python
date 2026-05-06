#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 20:14
# @Author      : Jim
# @File        : Solution03.py
# @Software    : PyCharm
# @Description :
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化哈希集合，用于存储当前窗口内的字符（保证无重复）
        char_set = set()
        # 左指针，初始化为0，代表窗口的左边界
        left = 0
        # 记录最长无重复子串的长度，初始化为0
        max_len = 0

        # 右指针遍历字符串，代表窗口的右边界
        for right in range(len(s)):
            # 关键：如果当前字符已经在集合中（说明有重复），需要移动左指针，直到移除重复字符
            while s[right] in char_set:
                # 从集合中移除左指针指向的字符
                char_set.remove(s[left])
                # 左指针右移，缩小窗口
                left += 1
            # 将当前右指针指向的字符加入集合（此时窗口内无重复）
            char_set.add(s[right])
            # 更新最长子串长度：当前窗口长度（right - left + 1）与历史最大值比较
            max_len = max(max_len, right - left + 1)

        # 返回最长无重复子串的长度
        return max_len