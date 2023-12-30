#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/12/17 23:42
# @Author      : Jim
# @File        : Solution700.py
# @Software    : PyCharm
# @Description :

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            return root

        left_search = self.searchBST(root.left, val)
        right_search = self.searchBST(root.right, val)

        if left_search:
            return left_search
        elif right_search:
            return right_search
        else:
            return None