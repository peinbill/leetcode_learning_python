#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/18 18:50
# @Author      : Jim
# @File        : Solution102.py
# @Software    : PyCharm
# @Description :
from collections import deque
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while len(queue)>0:
            tmp_len = len(queue)
            tmp_result = []

            for i in range(tmp_len):
                node = queue.popleft()
                tmp_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            result.append(tmp_result)


        return result