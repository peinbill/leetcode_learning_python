# -*- encoding: utf-8 -*-
"""
@File    : Solution3.py
@Time    : 2023/8/16 6:36 上午
@Author  : huangjinyu
@Desc   : 
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 经典滑动窗格问题

        @param s:
        @return:
        """
        n = len(s)
        if n==0:
            return 0

        left,right = 0,0
        max_len = 0
        tmp_set = set()
        for right in range(n):
            ch = s[right]
            if ch in tmp_set:
                while ch in tmp_set:
                    ch_left = s[left]
                    left += 1
                    tmp_set.remove(ch_left)
            else:
                max_len = max(max_len,right-left+1)
            tmp_set.add(ch)
            right += 1
        return max_len
