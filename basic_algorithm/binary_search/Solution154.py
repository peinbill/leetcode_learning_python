
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        if nums[left] < nums[right]:
            return nums[left]

        while left + 1 < right:
            mid = (left+right)//2

            if nums[mid] > nums[left]:
                left = mid+1
            else:
                left += 1
                right = mid

        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]

if __name__ == "__main__":
    solution = Solution()
    solution.findMin([10,1,10,10,10])