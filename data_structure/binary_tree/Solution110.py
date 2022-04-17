#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution110.py
@time: 2022/4/16 22:15
@Describe:
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return abs(self.max_hight(root.left)-self.max_hight(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def max_hight(self,root:TreeNode) -> int:
        if root is None:
            return 0
        return 1+max(self.max_hight(root.left),self.max_hight(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        """ 自低向上的递归

        :param root:
        :return:
        """
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
