from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2)<len(s1):
            return False

        cnt = Counter(s1)
        need = len(s1)

        len_s1 = len(s1)

        n = len(s2)

        left = right = 0

        for right in range(n):
            ch = s2[right]
            if ch in cnt:
                if cnt[ch] > 0:
                    need -= 1
                cnt[ch] -= 1

            while need == 0:
                if right - left + 1 == len_s1:
                    return True
                elif right - left + 1 > len_s1:
                    ch = s2[left]
                    if ch in cnt:
                        if cnt[ch] >= 0:
                            need += 1
                        cnt[ch] += 1
                    left += 1
        return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    solution = Solution()
    solution.checkInclusion(s1,s2)