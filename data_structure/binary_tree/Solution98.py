#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution98.py
@time: 2022/4/18 20:18
@Describe:
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """ 中序遍历的应用

        :param root:
        :return:
        """

        if root is None:
            return True

        order_list = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            order_list.append(node.val)
            inorder(node.right)

        inorder(root)
        val = -float("inf")
        for i in order_list:
            if i <= val:
                return False
            val = i
        return True

    def isValidBST2(self, root: TreeNode) -> bool:
        """ 基于递归方法

        :param root:
        :return:
        """

        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)







