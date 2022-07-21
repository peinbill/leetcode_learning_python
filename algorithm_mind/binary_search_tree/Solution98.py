# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        inorder_list = []
        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            inorder_list.append(node.val)
            in_order(node.right)

        in_order(root)
        pre = inorder_list[0]

        for i in range(1,len(inorder_list)):
            if inorder_list[i]<=pre:
                return False
            else:
                pre = inorder_list[i]

        return True