from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        n = len(nums)

        def helper(idx, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                helper(i + 1, temp_list + [nums[i]])

        helper(0, [])
        return res

    result = []

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        # 记录走过的路径
        self.backtrack(nums, 0, track, res)
        return res

    def backtrack(self, nums, start, track, res):
        res.append(track[:])
        for i in range(start, len(nums)):
            # 做选择
            track.append(nums[i])
            # 回溯
            self.backtrack(nums, i + 1, track, res)
            # 撤销选择
            track.pop()


























