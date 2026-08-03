#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/3 23:40
# @Author      : Jim
# @File        : Solution49.py
# @Software    : PyCharm
# @Description :

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())