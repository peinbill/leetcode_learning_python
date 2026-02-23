class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return 0
        max_sub = s[0]
        dp = [[False for j in s] for i in s]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if j == i + 1 and s[j] == s[i]:
                    dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] == True:
                        dp[i][j] = True

                if dp[i][j] == True:
                    if j - i + 1 > len(max_sub):
                        max_sub = s[i:j + 1]

        return max_sub