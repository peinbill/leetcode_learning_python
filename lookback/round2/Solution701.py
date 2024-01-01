#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/1 22:15
# @Author      : Jim
# @File        : Solution701.py
# @Software    : PyCharm
# @Description : 算法思想-二叉搜索树

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
        return root
