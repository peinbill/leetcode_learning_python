from typing import List

class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     set_num = set()
    #     for i in nums:
    #         set_num.add(i)
    #     left = list()
    #     for i in range(1,len(nums)+1):
    #         if i not in set_num:
    #             left.append(i)

    #     return left

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [idx + 1 for idx, num in enumerate(nums) if num > 0]