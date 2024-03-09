#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 01:56
# @Author      : Jim
# @File        : Solution701.py
# @Software    : PyCharm
# @Description :

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        root_val = root.val
        if root_val>val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)

        return root