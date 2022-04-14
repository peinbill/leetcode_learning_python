#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution94.py
@time: 2022/4/14 21:28
@Describe:
"""
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ 常见的递归做法

        :param root:
        :return:
        """
        rtn_list = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            rtn_list.append(node.val)
            inorder(node.right)

        inorder(root)
        return rtn_list

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        ret = []
        stack.append((0, root))

        while len(stack) != 0:
            op, node = stack.pop()
            if node is None:
                continue
            if op == 1:
                ret.append(node.val)
            else:
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
        return ret

    # 作者：forestsking
    # 链接：https: // leetcode - cn.com / problems / binary - tree - inorder - traversal / solution / by - forestsking - 95
    # fk /
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。