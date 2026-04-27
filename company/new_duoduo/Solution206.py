#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/4/27 23:11
# @Author      : Jim
# @File        : Solution206.py
# @Software    : PyCharm
# @Description :
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        current = head

        while current and current.next:
            next = current.next
            next_next = next.next

            current.next = next_next
            next.next = dummy.next  # 难点
            dummy.next = next

        return dummy.next