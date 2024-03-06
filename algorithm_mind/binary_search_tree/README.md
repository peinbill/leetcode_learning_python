# 二叉搜索树


优先考虑使用递归方式进行解决

定义

    每个节点中的值必须大于（或等于）存储在其左侧子树中的任何值。
    每个节点中的值必须小于（或等于）存储在其右子树中的任何值。

    简单来讲就是左边但比它小，右边但比它大

Solution98: 等价于中序遍历，在之前的基础算法算过

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.help(root,-float(inf),float(inf))
    
    def help(self,node,left_max,right_min):
        if node is None:
            return True
        val = node.val
        if left_max>=val or right_min=<val:
            return False
        
        return self.help(node.left,left_max,node.val) and self.help(node.right,node.val,right_min)
```

Solution701: 直接利用二叉搜索树的性质使用递归即可

Solution450：递归方法，就是处理各种其他问题的时候比较繁琐
找到以后直接找右子树的最小值

Solution110: 利用二叉树高度+递归