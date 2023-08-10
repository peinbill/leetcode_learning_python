# 二分查找的三个模板：
https://leetcode.cn/leetbook/read/binary-search/xe5fpe/  


熟练掌握3个模板即可

模板1：二分查找的最基础和最基本的形式。这是一个标准的二分查找模板
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
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
```

模板2：二分查找的高级模板。它用于查找需要访问数组中当前索引及其直接右邻居索引的元素或条件
```python

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1
```

模板3: 用于搜索需要访问当前索引及其在数组中的直接左右邻居索引的元素或条件。
理论上该模板是最万能的
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

实际过程中，掌握好1，3两个模板即可

Solution704:二分查找模板一

Solution35: 二分查找模板二，也可以使用模板3后再进行判断（理论上模板3是万能的）

Solution278: 二分查找模板三

Solution153: 部分有序，二分查找模板3

Solution154: 非模板1,2,3 https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/
可以使用模板3，核心在于需要跟右边界进行比较

只要保证开区间右端点在最小值或者最小值右侧就行，因为我们就是根据这一点来比较的。

如果mid选择和右边界比较，当 mid 和 end相等时，mid向左看，一定是先局部下降的，所以可以end-- 找最小值
如果mid选择和左边界比较，当 mid 和 start相等时，mid向右看，一定是先局部上升的，所以只适合通过start++找最大值


Solution33: 153的基础上再进一步(没有153做前提很难)

Solution81: Solution704的改进，多加一个条件。（不要完全死记硬背东西）

Solution74: 难点在于初始条件的构造，其实就是将矩阵转成数组




