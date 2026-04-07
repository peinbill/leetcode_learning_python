#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/6 20:43
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
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1