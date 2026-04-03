#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/3 23:47
# @Author      : Jim
# @File        : Solution98.py
# @Software    : PyCharm
# @Description :

# Definition for a binary tree node.

from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.help(root, -float("inf"), float("inf"))

    def help(self, node, left_max, right_min):
        if node is None:
            return True
        val = node.val
        if left_max >= val or right_min <= val:
            return False

        return self.help(node.left, left_max, node.val) and self.help(node.right, node.val, right_min)