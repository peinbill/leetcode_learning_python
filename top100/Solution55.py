


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_len = 0
        nums_len = len(nums)-1

        for i in range(len(nums)):
            if i > max_len:
                break
            max_len = max(max_len,i+nums[i])
            if max_len >= nums_len:
                return True

        return False