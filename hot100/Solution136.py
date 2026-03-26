from functools import reduce
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums_sorted = sorted(nums)

        for i in range(0, len(nums_sorted), 2):
            if i == len(nums_sorted) - 1:
                return nums_sorted[i]
            if nums_sorted[i] == nums_sorted[i + 1]:
                continue
            else:
                return nums_sorted[i]


