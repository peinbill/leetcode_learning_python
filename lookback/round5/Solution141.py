#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/9 17:52
# @Author      : Jim
# @File        : Solution141.py
# @Software    : PyCharm
# @Description : 环形检测

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False