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
        """ 递归，基于函数进行判断
        # TODO
        比较奇怪，java可以，Python出错
        :param root:
        :param p:
        :param q:
        :return:
        """

        ans = root
        def dfs(node,p,q):
            if node is None:
                return False

            left_dfs = dfs(node.left,p,q)
            right_dfs = dfs(node.right,p,q)

            if (left_dfs and right_dfs) or ((p==node or q==node) and (left_dfs or right_dfs)):
                ans = root
            return left_dfs or right_dfs or (node==p or node==q)

        dfs(root,p,q)
        return ans

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 分治法，有左子树的公共祖先或者有右子树的公共祖先，就返回子树的祖先，否则返回根节点

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



