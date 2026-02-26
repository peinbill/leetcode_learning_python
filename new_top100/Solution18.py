from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        nums.sort()
        for i in range(len(nums) - 3):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            rtn = self.threeSum(nums, i + 1, target - nums[i])
            if rtn:
                for rtn_2, rtn_3, rtn4 in rtn:
                    tmp_result = [nums[i], rtn_2, rtn_3, rtn4]
                    result.append(tmp_result)
        return result

    def threeSum(self, nums: List[int], start, target: int) -> List[List[int]]:
        result = list()
        for i in range(start, len(nums) - 2):
            if i > start and nums[i] == nums[i - 1]:
                continue
            rtn = self.twoSum(nums, i + 1, len(nums) - 1, target - nums[i])
            if rtn:
                for rtn_1, rtn_2 in rtn:
                    tmp_result = [nums[i], rtn_1, rtn_2]
                    result.append(tmp_result)

        return list(result)

    def twoSum(self, nums, start, end, target):
        result_set = set()
        result = []
        while start < end:
            if nums[start] + nums[end] == target:
                if (nums[start], nums[end]) not in result_set:
                    result.append((nums[start], nums[end]))
                    result_set.add((nums[start], nums[end]))
                start += 1
                end -= 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1

        return result