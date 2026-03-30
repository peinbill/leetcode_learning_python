import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for k in range(1, n + 1):
            tempMin = []
            for i in range(1, int(math.sqrt(k)) + 1):
                tempMin.append(dp[k - i**2])
            dp[k] = 1 + min(tempMin)
        return dp[n]

# 作者：Xenodochial Mcclintockh0y
# 链接：https://leetcode.cn/problems/perfect-squares/solutions/2767066/wan-quan-ping-fang-shu-zi-wen-ti-di-tui-efpmr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。