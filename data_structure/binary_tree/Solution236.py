#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution236.py
@time: 2022/4/16 22:51
@Describe:
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 分治法，有左子树的公共祖先或者有右子树的公共祖先，就返回子树的祖先，否则返回根节点
        画图即可理解
        :param root:
        :param p:
        :param q:
        :return:
        """
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None



