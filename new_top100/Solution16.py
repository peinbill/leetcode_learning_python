from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mini_abs = float("inf")
        mini_value = float("inf")

        def twoSum(nums, start, end, old_value):
            nonlocal mini_abs, mini_value
            while start < end:
                if abs(nums[start] + nums[end] + old_value - target) < mini_abs:
                    mini_abs = abs(nums[start] + nums[end] + old_value - target)
                    mini_value = nums[start] + nums[end] + old_value


                elif nums[start] + nums[end] + old_value > target:
                    end -= 1
                else:
                    start += 1

        nums.sort()
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            twoSum(nums, i + 1, len(nums) - 1, nums[i])

        return mini_value