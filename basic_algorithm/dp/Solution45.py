
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        farest = 0
        step = 0
        for i in range(len(nums)-1):
            farest = max(farest,i+nums[i])
            if i>= end:
                end = farest
                step += 1

        return step