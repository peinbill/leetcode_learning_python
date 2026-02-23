from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_len = 1
        for i in range(1, len(s)):
            for j in range(i - 1, -1, -1):
                if s[j] != s[i] and s[j] not in s[j + 1:i + 1]:
                    max_len = max(max_len, i - j + 1)
                else:
                    break

        return max_len

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     def contain_duplicate(counter):
    #         for k,v in counter.items():
    #             if v>1:
    #                 return False
    #         return True
    #     if len(s) == 0:
    #         return 0
    #     max_sub_length = 1
    #     left,right = 0,0

    #     while right  < len(s):
    #         counter = Counter()

    #         c= s[right]
    #         if c not in counter:
    #             counter[c] = 1
    #         else:
    #             counter[c] += 1

    #         left = right -1
    #         while left < right and left>=0 and contain_duplicate(counter):

    #             d = s[left]
    #             if d not in counter:
    #                 counter[d] = 1
    #             else:
    #                 counter[d] += 1

    #             if contain_duplicate(counter):
    #                 max_sub_length = max(max_sub_length,right-left+1)
    #             left -= 1
    #         right += 1

    #     return max_sub_length

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     def boolean_shrink(window):
    #         for k,v in window.items():
    #             if v>1:
    #                 return True
    #         return False
    #     if len(s) == 0:
    #         return 0

    #     max_len = 1
    #     left,right = 0,0
    #     window = {}
    #     while right < len(s):
    #         ch = s[right]
    #         if ch in window:
    #             window[ch] = window[ch]+1
    #         else:
    #             window[ch] = 1

    #         while boolean_shrink(window):
    #             d = s[left]
    #             window[d] = window[d]-1
    #             left+= 1
    #         max_len = max(max_len,right-left+1)
    #         right += 1

    #     return max_len