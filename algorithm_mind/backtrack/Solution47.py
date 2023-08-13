
from typing import List


class Solution:
    def __init__(self) -> None:

        self.res = []  # 用于存储结果
        self.track = []  # 用于存储路径
        self.used = []  # 记录元素是否使用过

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 先排序，让相同的元素靠在一起
        nums.sort()
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res

    def backtrack(self, nums):
        if len(self.track) == len(nums):
            self.res.append(self.track.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            # 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue
            self.track.append(nums[i])
            self.used[i] = True
            self.backtrack(nums)
            self.track.pop()
            self.used[i] = False
