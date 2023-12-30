#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 22:08
# @Author  : Jim
# @File    : Solution141.py
# @Software: PyCharm
# 数据结构-链表
# 经典快慢指针题目

from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        if head is None or head.next is None:
            return False

        while slow and fast:
            slow = slow.next
            fast = fast.next

            if fast is None:
                break
            fast = fast.next

            if slow is fast:
                return True
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        """ 标准答案，使用fast进行判断

        :param head:
        :return:
        """
        # 快慢指针初始化指向 head
        slow, fast = head, head
        # 快指针走到末尾时停止
        while fast and fast.next:
            # 慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next
            # 快慢指针相遇，说明含有环
            if slow == fast:
                return True
        # 不包含环
        return False