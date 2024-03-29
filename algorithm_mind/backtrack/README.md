# 回溯法

回溯法（backtrack）常用于遍历列表所有子集，是 DFS 深度搜索一种，
一般用于全排列，穷尽所有可能，遍历的过程实际上是一个决策树的遍历过程。
时间复杂度一般 O(N!)，它不像动态规划存在重叠子问题可以优化，
回溯算法就是纯暴力穷举，复杂度一般都很高。

常见问题：

排列/组合/子集求解

模板

```
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

```

解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件

其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」，特别简单。

Solution78: 直接使用模板进行求解即可

Solution90: 在78的基础上加入了排序逻辑以及去重逻辑（排序逻辑也是用于去重）

Solution46: 加入tmplist和visited数组

Solution47: 在Solution46的基础上加入校验重复逻辑
但是注意排列问题的剪枝逻辑，和子集/组合问题的剪枝逻辑略有不同：新增了 !used[i - 1] 的逻辑判断。










