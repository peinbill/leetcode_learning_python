# -*- encoding: utf-8 -*-
"""
@File    : Solution41.py
@Time    : 2023/10/30 10:47 下午
@Author  : huangjinyu
@Desc   : 
"""

from typing import List



# 原地哈希就相当于，让每个数字n都回到下标为n-1的家里。
#
# 而那些没有回到家里的就成了孤魂野鬼流浪在外，他们要么是根本就没有自己的家（数字小于等于0或者大于nums.size()），要么是自己的家被别人占领了（出现了重复）。
#
# 这些流浪汉被临时安置在下标为i的空房子里，之所以有空房子是因为房子i的主人i+1失踪了（数字i+1缺失）。
#
# 因此通过原地构建哈希让各个数字回家，我们就可以找到原始数组中重复的数字还有消失的数字。


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ 暴力破解法，但这并没有达到题目中说O(常数级)的空间复杂度

        @param nums:
        @return:
        """
        start = 1
        set_nums = set()
        for i in nums:
            set_nums.add(i)

        while True:
            if start in set_nums:
                start += 1

            else:
                return start


class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
