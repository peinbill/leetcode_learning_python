#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution102.py
@time: 2022/4/16 21:51
@Describe:
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        rtn_list = []
        if not root:
            return rtn_list

        queue = deque(root)

        while len(queue) > 0:
            level = []
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            rtn_list.append(level)

        return rtn_list

