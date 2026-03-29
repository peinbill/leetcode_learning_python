from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        total = sum(nums)

        if total % 2 != 0:
            return False
        bag = total // 2

        dp = [[0 for j in range(bag + 1)] for i in range(len(nums) + 1)]
        for row in range(1, len(nums) + 1):
            for column in range(1, bag + 1):
                if column - nums[row - 1] >= 0:
                    dp[row][column] = max(dp[row - 1][column], nums[row - 1] + dp[row - 1][column - nums[row - 1]])
                else:
                    dp[row][column] = dp[row - 1][column]
        return dp[-1][-1] == bag