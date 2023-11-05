# -*- encoding: utf-8 -*-
"""
@File    : Solution23.py
@Time    : 2023/10/8 8:56 上午
@Author  : huangjinyu
@Desc   :

方法一：两两合并上进行演进


"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        val1 = list1.val
        val2 = list2.val
        if val1 < val2:
            rtn = ListNode(val1)
            rtn.next = self.mergeTwoLists(list1.next, list2)
        else:
            rtn = ListNode(val2)
            rtn.next = self.mergeTwoLists(list1, list2.next)
        return rtn

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) > 0:
            head = lists[0]
        else:
            return None
        for l in lists[1:]:
            head = self.mergeTwoList(head, l)
        return head


import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = [CmpNode(head) for head in lists if head]  # 初始将所有链表头节点转为可比较节点入队
        heapq.heapify(queue)  # 进行初始的小顶堆堆话，相当于对每个链表的头节点排序
        pre = ListNode()  # 伪头节点
        node = pre  # 当前合并链表的最后一个节点
        # 合并链表直到队列不为空
        while queue:
            node.next = heapq.heappop(queue).ori_node  # 弹出当前节点值最小的可比较节点，合并链表的新节点就是这个可比较节点的原始节点
            node = node.next  # 更新node指向，指向最小值节点
            if node.next:  # 当前节点还有下一个节点
                heapq.heappush(queue, CmpNode(node.next))  # 将最小值节点的下一个节点转为可比较节点入队
        return pre.next


class CmpNode:
    """
    可比较节点
    """

    def __init__(self, node: Optional[ListNode]):
        self.ori_node = node  # 原始节点

    def __lt__(self, other):
        return self.ori_node.val < other.ori_node.val  # 小于规则，根据原始节点值比较




