from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            res.append(bin(i).count("1"))
        return res

    def countBits2(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(1,num+1):
            if(i%2==1):
                dp[i]=dp[i-1]+1
            else:
                dp[i]=dp[i//2]
        return dp

# 作者：吴彦祖
# 链接：https://leetcode.cn/problems/counting-bits/solutions/56702/dong-tai-gui-hua-wei-yun-suan-xing-zhi-python3-by-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
