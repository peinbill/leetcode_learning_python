from collections import deque
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        rtn = []

        stack = deque([root])

        while stack:
            tmp_len = len(stack)
            tmp_result = []
            for i in range(tmp_len):
                tmp_node = stack.popleft()
                if tmp_node:
                    tmp_result.append(tmp_node.val)
                    stack.append(tmp_node.left)
                    stack.append(tmp_node.right)
            if tmp_result:
                rtn.append(tmp_result)

        return rtn