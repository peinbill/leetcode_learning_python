# -*- encoding: utf-8 -*-
"""
@File    : Solution7.py
@Time    : 2023/9/3 8:17 下午
@Author  : huangjinyu
@Desc   : 
"""
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0

