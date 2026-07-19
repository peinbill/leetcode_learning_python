根据 https://github.com/dashidhy/algorithm-pattern-python 进行刷题
每种类型候选抽取1题，用于快速更新知识

## 数据结构篇
- 二叉树

Solution104: 基于二叉树的特性使用递归

- 链表

Solution206：基于链表，记得画图

- 栈和队列

Solution102: 基于队列的应用


## 基础算法篇
- 二分搜索
Solution278: 基于二分查找模板3
```python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1
```


- 排序算法
（快排、归并、堆排序）
Solution912：快排

直接记住就行

- 动态规划
Solution322：需要记住，背包问题和零钱问题都是物品放在外面

## 算法思维篇
- 递归思维
Solution509: 直接根据递归思想即可


- 滑动窗格
Solution76: 直接根据模板即可，核心还是counter和need
python 版本
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
Solution701: 按照此特性写

- 回溯法
Solution78：掌握好回溯法的公式
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