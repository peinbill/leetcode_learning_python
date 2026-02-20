#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/18 18:03
# @Author      : Jim
# @File        : Solution92.py
# @Software    : PyCharm
# @Description :

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        pre = dummy
        current = head
        for i in range(left - 1):
            pre = pre.next
            current = current.next

        for i in range(right - left):
            next = current.next
            current.next = next.next
            next.next = pre.next
            pre.next = next

        return dummy.next