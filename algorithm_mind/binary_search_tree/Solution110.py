# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxHeight(node: TreeNode):
            if node is None:
                return 0
            return max(maxHeight(node.left),
                       maxHeight(node.right)) + 1
        if root is None:
            return True
        return abs(maxHeight(root.left)-maxHeight(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

