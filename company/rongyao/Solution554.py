#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/23 17:02
# @Author      : Jim
# @File        : Solution554.py
# @Software    : PyCharm
# @Description : 等价转换
# https://leetcode.cn/problems/brick-wall/
from typing import List
import collections
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gapdict = collections.defaultdict(int)
        for wallline in wall:
            dis = 0
            for i in range(len(wallline)-1):
                dis+=wallline[i]
                gapdict[dis]+=1
        if len(gapdict.values())==0:
            return len(wall)
        return len(wall)-max(gapdict.values())
