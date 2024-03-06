#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/7 01:35
# @Author      : Jim
# @File        : Solution46.py
# @Software    : PyCharm
# @Description : 基于公式进行处理即可

from typing import List

class Solution:

    def __init__(self) -> None:
        self.result = []
        self.visited = set()
        self.track = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(self.track,len(nums))

        return self.result

    def backtrack(self,nums):
        if len(self.track) == len(nums):
            self.result.append(self.track[:])
            return

        for i in range(len(nums)):
            if nums[i] in self.visited:
                continue

            self.track.append(nums[i])
            self.visited.add(nums[i])
            self.backtrack(nums)
            self.track.pop()
            self.visited.remove(nums[i])