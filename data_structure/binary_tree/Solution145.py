#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution145.py
@time: 2022/4/14 22:24
@Describe:
"""
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        非递归做法，迭代并加入标记
        :param root:
        :return:
        """
        rtn_list = []
        stack = [(0,root)]
        while len(stack) > 0 :
            token,node = stack.pop()
            if not node:
                continue
            if token == 1:
                rtn_list.append(node)
            else:
                stack.append((1,node.val))
                stack.append((0,node.right))
                stack.append((0,node.left))
        return rtn_list

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """ 递归做法

        :param root:
        :return:
        """
        rtn_list = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            rtn_list.append(node.val)
        postorder(root)
        return rtn_list