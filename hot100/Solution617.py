from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return
        if root1 is None and root2:
            return root2
        if root2 is None and root1:
            return root1

        val1, val2 = 0, 0

        if root1:
            val1 = root1.val
        if root2:
            val2 = root2.val
        root1.val = val1 + val2
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1