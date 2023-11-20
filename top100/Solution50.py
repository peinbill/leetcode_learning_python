# -*- encoding: utf-8 -*-
"""
@File    : Solution36.py
@Time    : 2023/10/30 10:47 下午
@Author  : huangjinyu
@Desc   : 
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """ 递归+快速

        @param x:
        @param n:
        @return:
        """
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    def myPow2(self, x: float, n: int) -> float:
        """ 基于递归的方法，但是单纯使用递归会直接超时

        @param x:
        @param n:
        @return:
        """
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            x = 1/x
            n = abs(n)
        return x*self.myPow(x,n-1)