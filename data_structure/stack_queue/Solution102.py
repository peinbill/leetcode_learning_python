#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution102.py
@time: 2022/5/11 22:06
@Describe:
"""
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return_list = []
        if root is None:
            return return_list

        queue = deque([root])
        while queue:
            tmp_result = []
            queue_len = len(queue)
            for i in range(queue_len):
                tmp_node = queue.popleft()
                if tmp_node.left:
                    queue.append(tmp_node.left)

                if tmp_node.right:
                    queue.append(tmp_node.right)

                tmp_result.append(tmp_node.val)
            return_list.append(tmp_result)

        return return_list