# -*- encoding: utf-8 -*-
"""
@File    : Solution36.py
@Time    : 2023/10/30 10:47 下午
@Author  : huangjinyu
@Desc   : 
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        self.visit = [False for i in nums]

        # 记录走过的路径
        self.backtrack(nums, track, res)
        return res

    def backtrack(self, nums, track, res):
        if len(track) == len(nums):
            res.append(track[:])
            return
        for i in range(len(nums)):
            if self.visit[i]:
                continue
            # 做选择
            track.append(nums[i])
            self.visit[i] = True

            # 回溯
            self.backtrack(nums, track, res)

            # 撤销选择
            track.pop()
            self.visit[i] = False
