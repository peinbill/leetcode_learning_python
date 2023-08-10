#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
from cmath import e
from random import random
from typing import List
from importlib.metadata import PathDistribution


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def heap_sort(self, nums: List[int]) -> List[int]:
        def swim(arr, i, end):
            j = 2 * i
            while j <= end:
                if j + 1 <= end and arr[j + 1] > arr[j]:
                    j += 1

                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i = j
                    j = 2 * i
                else:
                    break

        nums = [0] + nums

        len_nums = len(nums)
        # 构造堆
        for i in range((len_nums - 1) // 2, 0, -1):
            swim(nums, i, len_nums - 1)

        # 堆排序
        for i in range(len_nums - 1, 0, -1):
            nums[1], nums[i] = nums[i], nums[1]
            swim(nums, 1, i - 1)

        return nums[1:]

    def sortArray(self, nums: List[int]) -> List[int]:
        """ 堆排序-有注释版

        @param nums:
        @return:
        """

        def maxHepify(arr, i, end):  # 大顶堆
            j = 2 * i  # j为i的左子节点【建堆时下标1表示堆顶】
            while j <= end:
                if j + 1 <= end and arr[j + 1] > arr[j]:  # i的左右子节点分别为j和j+1
                    j += 1  # 取两者之间的较大者

                if arr[i] < arr[j]:  # 若i指示的元素小于其子节点中的较大者
                    arr[i], arr[j] = arr[j], arr[i]  # 交换i和j的元素，并继续往下判断
                    i = j  # 往下走：i调整为其子节点j
                    j = 2 * i  # j调整为i的左子节点
                else:  # 否则，结束调整
                    break

        n = len(nums)
        nums = [0] + nums  # nums头部添加0，满足从下标1开始建堆

        # 建堆【大顶堆】
        for i in range(n // 2, 0, -1):  # 从第一个非叶子节点n//2开始依次往上进行建堆的调整【注意：此时堆顶为下标1】
            maxHepify(nums, i, n)

        # 排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆
        for j in range(n, 0, -1):
            nums[1], nums[j] = nums[j], nums[1]  # nums[1]为堆顶元素（最大值），将其放置到尾部j
            maxHepify(nums, 1, j - 1)  # j-1变成尾部，并从堆顶1开始调整堆

        return nums[1:]

    def merge_sort(self, nums: List[int]) -> List[int]:
        def merge(A, B):
            C = []
            i, j = 0, 0
            while i < len(A) and j < len(B):
                if A[i] < B[j]:
                    C.append(A[i])
                    i += 1
                else:
                    C.append(B[j])
                    j += 1

            while i < len(A):
                C.append(A[i])
                i += 1

            while j < len(B):
                C.append(B[j])
                j += 1
            return C

        def mergeSort(nums):
            n = len(nums)
            if n < 2:
                return nums
            left = mergeSort(nums[:n // 2])
            right = mergeSort(nums[n // 2:])
            return merge(left, right)

        nums = mergeSort(nums)
        return nums

    def quick_sort(self, nums: List[int]) -> List[int]:
        """
            使用快速排序
        """

        def quickSort(nums, l, r):
            while l >= r:
                return

            pivort = partition(nums, l, r)

            quickSort(nums, l, pivort - 1)
            quickSort(nums, pivort, r)

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

        quickSort(nums, 0, len(nums) - 1)

        return nums
