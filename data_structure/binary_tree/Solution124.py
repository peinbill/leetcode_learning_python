#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution124.py
@time: 2022/4/16 22:32
@Describe:
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值-这一点优点难理解，还是画个图就好
            # 因为作为返回的路径，它是不能左右子节点都加起来的
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum



    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """ 该方法是错误的，在于没有考虑负数以及整个链条的打通

        :param root:
        :return:
        """
        if root is None:
            return -float("inf")

        node_val = root.val
        left_max = self.maxPathSum(self.maxPathSum)
        right_max = self.maxPathSum(self.maxPathSum)

        return max(node_val, left_max, right_max, left_max + node_val, right_max + node_val,
                   left_max + node_val + right_max)