#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 23:31
# @Author  : Jim
# @File    : Solution102.py
# @Software: PyCharm

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
        queue = [root]
        result = []

        while len(queue)>0:
            queue_len = len(queue)
            tmp_result = []

            for i in range(queue_len):
                out = queue.pop()
                if out.left:
                    queue.insert(0,out.left)
                if out.right:
                    queue.insert(0,out.right)
                tmp_result.append(out.val)

            result.append(tmp_result)
        return result