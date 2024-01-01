#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2023/12/31 10:37
# @Author      : Jim
# @File        : Solution141.py
# @Software    : PyCharm
# @Description : 链表-基于快慢指针，唯一的难点在与快慢指针的判断

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
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