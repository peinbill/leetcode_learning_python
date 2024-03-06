#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/3 21:34
# @Author      : Jim
# @File        : Solution98.py
# @Software    : PyCharm
# @Description : 数据结构-二叉树
# 解法1：使用了中序遍历的性质
# 解法2：递归

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isValidBST2(self, root: TreeNode) -> bool:
        return self.helper(root, None, None)

    # 限定以 root 为根的子树节点必须满足 max.val > root.val > min.val
    def helper(self, root, min_node, max_node):
        # base case
        if not root:
            return True
        # 若 root.val 不符合 max 和 min 的限制，说明不是合法 BST
        if min_node and root.val <= min_node.val:
            return False
        if max_node and root.val >= max_node.val:
            return False
        # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
        return self.helper(root.left, min_node, root) and self.helper(root.right, root, max_node)

    def __init__(self) -> None:
        self.inorder_list = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 二叉搜索树
        self.inorder(root)

        for i in range(len(self.inorder_list)-1):
            pre = self.inorder_list[i]
            post = self.inorder_list[i+1]
            if pre >= post:
                return False
        return True


    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        self.inorder_list.append(node.val)
        self.inorder(node.right)