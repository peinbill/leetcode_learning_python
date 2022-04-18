#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution01.py
@time: 2022/4/18 20:38
@Describe:
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """ 递归

        :param root:
        :param val:
        :return:
        """
        def insert(node, val):
            if node is None:
                return TreeNode(val)
            node_val = node.val
            if val < node_val:
                node.left = insert(node.left, val)
            else:
                node.right = insert(node.right, val)
            return node

        root = insert(root, val)
        return root

    def insertIntoBST2(self, root: TreeNode, val: int) -> TreeNode:
        """ 循环

        :param root:
        :param val:
        :return:
        """

        if root is None:
            return TreeNode(val)

        node = root
        while True:
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left