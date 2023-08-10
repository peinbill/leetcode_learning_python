# 排序算法

3个排序方法：

1. 快速排序 选择切分点，再递归

核心在于切分点的选择

```python
import random

def partition(nums, l, r):
    pirot = random.randint(l, r)
    # 先随机选择数据，再跟最后一个数进行交换
    nums[pirot], nums[r] = nums[r], nums[pirot]
    p = nums[r]
    i = l
    for j in range(l, r):
        if nums[j] <= p:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i

```

2. 归并排序 先递归，再合并

归并排序是稳定的，但是需要多一个辅助队列

代码难度

3. 堆排序 先构成堆，再进行堆排序

核心在与掌握swim函数

构建堆：从非叶子节点进行swim往上

堆排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆（也是基于swim）
