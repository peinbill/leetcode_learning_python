
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums,target):
            left,right = 0,len(nums)-1
            while left<= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return True
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid -1
            return False
        flat = []
        for row in matrix:
            flat.extend(row)

        return binarySearch(flat,target)