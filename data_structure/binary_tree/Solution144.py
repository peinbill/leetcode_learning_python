#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution144.py
@time: 2022/4/13 22:07
@Describe:
"""
# Definition for a binary tree node.
from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ 使用递归做法

        :param root:
        :return:
        """
        rtn_list = []
        def preorder(node):
            if not node:
                return
            rtn_list.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return rtn_list

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """ 非递归做法本质可以使用图

        :param root:
        :return:
        """
        rtn_list = []
        if root is None:
            return rtn_list

        stack = [root]

        while len(stack)>0:
            node = stack.pop()
            rtn_list.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return rtn_list

