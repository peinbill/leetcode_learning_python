#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/1 22:33
# @Author      : Jim
# @File        : Solution46.py
# @Software    : PyCharm
# @Description :算法思想-回溯法

from typing import List

class Solution:
    def __init__(self) -> None:
        self.result = []
        self.visited = set()
        self.track = []


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums,len(nums))
        return self.result

    def backtrack(self,nums,_len):
        if len(self.track) == _len:
            self.result.append(self.track[:])
            return

        for i in nums:
            if i not in self.visited:
                self.track.append(i)
                self.visited.add(i)
                self.backtrack(nums,_len)
                self.track.pop()
                self.visited.remove(i)