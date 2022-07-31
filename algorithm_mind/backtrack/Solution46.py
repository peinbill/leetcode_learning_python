from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        res = []
        n = len(nums)
        visited = [0] * n

        def helper(temp_list, length):
            if length == n:
                res.append(temp_list)
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = 1
                helper(temp_list + [nums[i]], length + 1)
                visited[i] = 0
        helper([],0)
        return res


