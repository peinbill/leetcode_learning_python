#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/17 18:42
# @Author      : Jim
# @File        : Solution110.py
# @Software    : PyCharm
# @Description :
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