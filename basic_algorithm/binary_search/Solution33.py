from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        def binary_search(left, right):
            while left <= right:
                mid = (left+right)//2
                if target == nums[mid]:
                    return mid
                elif target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid+1

            return -1

        def find_min_index(nums):
            left = 0
            right = len(nums)-1
            while left+1<right:
                if nums[left]<nums[right]:
                    return left
                mid = (left+right)//2
                if nums[mid]>nums[left]:
                    left = mid
                else:
                    right = mid
            if nums[left]<nums[right]:
                return left
            else:
                return right

        idx = find_min_index(nums)

        left_search = binary_search(0,idx-1)
        if left_search != -1:
            return left_search
        right_search = binary_search(idx,len(nums)-1)

        if right_search != -1:
            return right_search

        return -1



