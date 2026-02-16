# leetcode_learning_python

记录leetcode刷题（使用python语言）


参考网站：

`https://github.com/greyireland/algorithm-pattern/blob/master/data_structure/binary_tree.md
`
https://github.com/dashidhy/algorithm-pattern-python


# 核心内容

## 数据结构篇
- 二叉树
```text
常考点：前/中/后序遍历

递归和分治法

DFS 深度搜索（从上到下） 和分治法区别：前者一般将最终结果通过指针参数传入，后者一般递归返回结果最后合并

分治法应用:  
先分别处理局部，再合并结果

适用场景
- 快速排序
- 归并排序 
- 二叉树相关问题

分治法模板
- 递归返回条件
- 分段处理
- 合并结果

```


- 链表
```
在做链表的题目时，核心的要点就是......画图

常用技巧：
null/nil 异常处理
dummy node 哑巴节点
快慢指针
```


- 栈和队列

```text
栈：先进后出
队：先进先出
在python更多可以用列表或者deque进行模拟
比较难的题一般为单调栈/单调队列

```


## 基础算法篇
- 二分搜索
```text
熟练掌握二分搜索的3个模板，尤其是1，3模版

掌握局部有序的概念
```  


- 排序算法
```text
掌握3种常考的排序方式，分别是：
1. 快速排序
核心在于切分点的选择


2. 归并排序
归并排序是稳定的，但是需要多一个辅助队列

3. 堆排序
核心在与掌握swim函数
构建堆：从非叶子节点进行swim往上
堆排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆（也是基于swim）

```  


- 动态规划
```text
四点要素

状态 State
    灵感，创造力，存储小规模问题的结果
方程 Function
    状态之间的联系，怎么通过小的状态，来算大的状态
初始化 Intialization
    最极限的小状态是什么, 起点
答案 Answer
    最大的那个状态是什么，终点

```  


- 图
```text
其实图就是多叉树的基础上加入visited

路径题目：

union-find->kruskal最小生成树->Prim最小生成树->Dijkstra


```


## 算法思维篇
- 递归思维
```text
将大问题转化为小问题，通过递归依次解决各个小问题

```  

- 滑动窗格
```python
def slidingWindow(s: str):
    # 用合适的数据结构记录窗口中的数据
    window = {}
    
    left = 0
    right = 0
    
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        if c not in window:
            window[c] = 1
        else:
            window[c] += 1
            
        # 增大窗口
        right += 1
        
        # 进行窗口内数据的一系列更新
        # ...
        
        # 判断左侧窗口是否要收缩
        while left < right and window needs shrink:
            # d 是将移出窗口的字符
            d = s[left]
            
            # 缩小窗口
            left += 1
            
            # 进行窗口内数据的一系列更新
            # ...

```
- 二叉搜索树
```text
每个节点中的值必须大于（或等于）存储在其左侧子树中的任何值。
每个节点中的值必须小于（或等于）存储在其右子树中的任何值。


```  

- 回溯法
```text
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


```text
解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件

其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」，特别简单。


```