from typing import List
class Solution:
    def firstMissingPositive2(self, nums: List[int]) -> int:
        start = 1
        set_nums = set()
        for i in nums:
            set_nums.add(i)

        while True:
            if start in set_nums:
                start += 1

            else:
                return start

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1