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