# -*- encoding: utf-8 -*-
"""
@File    : Solution36.py
@Time    : 2023/10/30 10:47 下午
@Author  : huangjinyu
@Desc   : 
"""

from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())