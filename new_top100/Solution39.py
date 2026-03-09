from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def brack_track(i):
            if i>=len(candidates) or sum(result)>target:
                return
            if sum(result) == target and result not in results:
                results.append(result.copy())
            for j in range(i,len(candidates)):
                result.append(candidates[j])
                brack_track(j)
                result.pop()
        result = []
        results = []
        brack_track(0)
        return results