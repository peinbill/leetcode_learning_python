
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ 基于动态规划

        @param nums:
        @return:
        """
        nums_result = nums.copy()
        for i in range(1, len(nums)):
            nums_result[i] = max(nums_result[i - 1] + nums[i], nums[i])

        return max(nums_result)