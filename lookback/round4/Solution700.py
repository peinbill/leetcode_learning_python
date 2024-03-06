#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/7 01:25
# @Author      : Jim
# @File        : Solution700.py
# @Software    : PyCharm
# @Description : 根据左边的比它小，右边的比它大的二叉搜索树的性质即可得到


from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)