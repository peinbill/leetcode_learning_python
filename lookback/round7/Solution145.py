from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn = []

        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            rtn.append(node.val)

        postorder(root)
        return rtn