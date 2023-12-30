#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 21:24
# @Author  : Jim
# @File    : Solution104.py
# @Software: PyCharm
# 数据结构-二叉树题目
# 核心在于使用使用递归

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root

        if root is p or root is q:
            return root

        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        if left_result and right_result:
            return root
        if left_result:
            return left_result
        if right_result:
            return right_result
        return None