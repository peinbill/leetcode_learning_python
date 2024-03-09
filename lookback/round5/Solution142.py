#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/9 17:52
# @Author      : Jim
# @File        : Solution142.py
# @Software    : PyCharm
# @Description : 快慢指针+画图计算

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        meet_node = self.hasCycle(head)

        if meet_node:
            current = head
            index = 0
            while current is not meet_node:
                current = current.next
                meet_node = meet_node.next
                index += 1
            return current

        else:
            return None

    def hasCycle(self, head: Optional[ListNode]):

        slow, fast = head, head

        while fast is not None and fast.next is not None and fast.next.next is not None:

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None
