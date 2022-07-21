class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0

        left,right = 0,0
        max_len = 0
        tmp_set = set()
        for right in range(n):
            ch = s[right]
            if ch not in tmp_set:
                max_len = max(max_len,right-left+1)
                tmp_set.add(ch)
                right += 1
            else:
                while ch in tmp_set:
                    ch_l = s[left]
                    tmp_set.remove(ch_l)
                    left += 1
                tmp_set.add(ch)
                right += 1
        return max_len