from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_common_k = counter.most_common(k)
        result = []
        for k,v in most_common_k:
            result.append(k)
        return result