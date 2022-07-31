
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []
        n = len(nums)
        visited = [0] * n

        def backtrack(tmplist,tmpLength):
            if tmpLength == n and tmplist not in result:
                result.append(tmplist)

            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = 1
                backtrack(tmplist + [nums[i]], tmpLength + 1)
                visited[i] = 0
        backtrack([],0)
        return result
