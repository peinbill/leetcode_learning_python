#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution104.py
@time: 2022/4/16 22:04
@Describe:
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional,List
import collections

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    def maxDepth(self, root: TreeNode) -> List[List[int]]:

        depth = 0
        if root is None:
            return depth

        bfs = collections.deque([root])

        while len(bfs) > 0:
            depth += 1
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)

        return depth