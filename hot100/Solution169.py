from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter()
        for i in nums:
            cnt.update([i])

        for k, v in cnt.items():
            if v > len(nums) / 2:
                return k
