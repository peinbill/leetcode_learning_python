#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution103.py
@time: 2022/4/17 20:29
@Describe:
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """ BFS多加一个token
        """
        ans_list = []

        if root is None:
            return ans_list

        _queue = deque([root])

        ascend = True

        while len(_queue) > 0:
            queue_len = len(_queue)
            tmp_list = []
            for _ in range(queue_len):
                node = _queue.popleft()
                tmp_list.append(node.val)
                if node.left is not None:
                    _queue.append(node.left)
                if node.right is not None:
                    _queue.append(node.right)

            if ascend:
                ans_list.append(tmp_list)
            else:
                ans_list.append(tmp_list[::-1])
            ascend = not ascend

        return ans_list