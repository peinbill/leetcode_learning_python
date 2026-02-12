from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn = []
        if root is None:
            return rtn
        left_node = self.preorderTraversal(root.left)
        right_node = self.preorderTraversal(root.right)
        rtn.append(root.val)
        rtn.extend(left_node)
        rtn.extend(right_node)
        return rtn