class Solution:
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """ 答案版

        :param text1:
        :param text2:
        :return:
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len = len(text1)
        text2_len = len(text2)
        rtn_matrix = [[0 for j in range(text1_len+1)] for i in range(text2_len+1)]

        for i in range(1,text2_len+1):
            # 列
            if text1[0] == text2[i-1]:
                rtn_matrix[i][1] = 1
            else:
                rtn_matrix[i][1] = rtn_matrix[i-1][1]


        for i in range(1,text1_len+1):
            # 行
            if text2[0] == text1[i-1]:
                rtn_matrix[1][i] = 1
            else:
                rtn_matrix[1][i] = rtn_matrix[1][i-1]

        for i in range(2,text2_len+1):
            for j in range(2,text1_len+1):
                if text1[j-1] == text2[i-1]:
                    rtn_matrix[i][j] = max(rtn_matrix[i-1][j],rtn_matrix[i][j-1])+1
                else:
                    rtn_matrix[i][j] = max(rtn_matrix[i-1][j],rtn_matrix[i][j-1])


        return rtn_matrix[-1][-1]





