from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        def brack_track(i):
            if i > len(candidates) or sum(result) > target:
                return

            if sum(result) == target and result not in results:
                results.append(result.copy())
            for j in range(i, len(candidates)):
                if j > i and candidates[i] == candidates[i - 1]:
                    continue
                result.append(candidates[j])
                brack_track(j + 1)
                result.pop()

        result = []
        results = []

        brack_track(0)
        return results