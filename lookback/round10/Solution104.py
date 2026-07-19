#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/18 22:26
# @Author      : Jim
# @File        : Solution104.py
# @Software    : PyCharm
# @Description :
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
