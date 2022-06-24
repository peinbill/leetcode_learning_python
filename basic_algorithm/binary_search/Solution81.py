from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        n = len(nums)
        if n == 1:
            return nums[0] == target

        l, r = 0, n - 1
        while l <= r:
            mid = l+(r-l) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid]:
                l += 1
                continue
            if nums[l] < nums[mid]:
                if nums[l]<= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return False


if __name__ == "__main__":
    solution = Solution()
    solution.search([1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1],13)






