
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        if nums[left] < nums[right]:
            return nums[left]

        while left + 1 < right:
            mid = (left+right)//2

            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid

        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
