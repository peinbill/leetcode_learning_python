#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/9 17:32
# @Author      : Jim
# @File        : Solution83.py
# @Software    : PyCharm
# @Description : 链表的基本操作

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = list(val=float("inf"),next=head)

        current = head

        while current and current.next:
            while current.val == current.next.val:
                current.next = current.next.next

        return dummy.next