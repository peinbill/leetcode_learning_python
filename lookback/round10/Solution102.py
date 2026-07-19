#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/18 23:29
# @Author      : Jim
# @File        : Solution102.py
# @Software    : PyCharm
# @Description :
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            tmp_result = []

            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                tmp_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp_result)
        return result