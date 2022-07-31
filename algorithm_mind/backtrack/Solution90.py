from typing import List


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        res = []
        nums.sort()

        def helper(idx, n, temp_list):
            if temp_list not in res:
                res.append(temp_list)
            for i in range(idx, n):
                helper(i + 1, n, temp_list + [nums[i]])

        helper(0,n,[])

        return  res