#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/16 10:59
# @Author      : Jim
# @File        : Solution98.py
# @Software    : PyCharm
# @Description :

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        sort_num = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            sort_num.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(len(sort_num) - 1):
            left = sort_num[i]
            right = sort_num[i + 1]
            if left >= right:
                return False

        return True