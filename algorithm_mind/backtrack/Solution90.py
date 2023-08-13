from typing import List


class Solution(object):
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        nums.sort()
        # 记录走过的路径
        self.backtrack(nums, 0, track, res)
        return res

    def backtrack(self, nums, start, track, res):
        res.append(track[:])
        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
            if i > start and nums[i] == nums[i-1]:
                continue
            # 做选择
            track.append(nums[i])
            # 回溯
            self.backtrack(nums, i + 1, track, res)
            # 撤销选择
            track.pop()