class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.getMaxPath(root)
        return self.maxSum

    def getMaxPath(self, root):
        if root is None:
            return 0
        left_max_path = max(self.getMaxPath(root.left), 0)
        right_max_path = max(self.getMaxPath(root.right), 0)

        root_max_path = root.val + left_max_path + right_max_path
        self.maxSum = max(self.maxSum, root_max_path)

        return root.val + max(left_max_path, right_max_path)