
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        farest = 0
        for i in range(len(nums[:-1])):
            farest = max(farest,i+nums[i])
            if farest<=i:
                return False

        return farest>=len(nums)-1