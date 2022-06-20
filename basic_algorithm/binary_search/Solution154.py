
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

if __name__ == "__main__":
    solution = Solution()
    solution.findMin([10,1,10,10,10])