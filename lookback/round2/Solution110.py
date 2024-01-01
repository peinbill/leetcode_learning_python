#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/12/30 23:30
# @Author      : Jim
# @File        : Solution110.py
# @Software    : PyCharm
# @Description : 二叉树的应用，在104的基础上进行进一步的提升

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_heigh = self.max_heigh(root.left)
        right_height = self.max_heigh(root.right)

        if abs(left_heigh - right_height) > 1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)

    def max_heigh(self, root):
        if root is None:
            return 0

        return 1 + max(self.max_heigh(root.left), self.max_heigh(root.right))
