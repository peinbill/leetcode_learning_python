from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        if len(p) > len(s):
            return result

        left, right = 0, 0

        cnt = collections.Counter(p)
        need = len(p)
        len_p = len(p)
        n = len(s)

        for right in range(n):
            ch = s[right]
            if ch in cnt:
                if cnt[ch] > 0:
                    need -= 1
                cnt[ch] -= 1

            while need == 0:
                if right - left + 1 == len_p:
                    result.append(left)

                ch = s[left]
                if ch in cnt:
                    if cnt[ch] >= 0:
                        need += 1
                    cnt[ch] += 1
                left += 1

        return result
