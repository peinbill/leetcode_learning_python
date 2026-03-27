# 01背包问题是选或者不选，但本题是必须选，是选+还是选-。先将本问题转换为01背包问题。
# 假设所有符号为+的元素和为x，符号为-的元素和的绝对值是y。
# 我们想要的 S = 正数和 - 负数和 = x - y
# 而已知x与y的和是数组总和：x + y = sum
# 可以求出 x = (S + sum) / 2 = target
# 也就是我们要从nums数组里选出几个数，令其和为target
# 于是就转化成了求容量为target的01背包问题 =>要装满容量为target的背包，有几种方案
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (target+sum(nums))%2!=0:
            return 0
        total = (target+sum(nums))//2 # 定义正数和为total
        if total<0: # 正数和为负，返回0
            return 0
        dp = [[0 for _ in range(total+1)] for _ in range(len(nums))]
        for j in range(total+1): # 初始化第一行
            if nums[0]==j:
                dp[0][j]=1
        dp[0][0]+=1 # 初始化第一行后，[0][0]自增1，到此才算初始化结束
        for i in range(1,len(nums)):
            for j in range(total+1):
                if j>=nums[i]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]