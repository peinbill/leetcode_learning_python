class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return -1
        n = len(needle)
        for i in range(0,len(haystack)-n+1):
            if needle == haystack[i:i+n]:
                return i

        return -1