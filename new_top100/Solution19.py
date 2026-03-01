#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/3/1 19:55
# @Author      : Jim
# @File        : Solution19.py
# @Software    : PyCharm
# @Description :
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k_current = head
        dummy = ListNode(next = head)
        current = dummy
        if k_current.next is None:
            return None

        for i in range(n):
            k_current = k_current.next

        while k_current and current:
            k_current = k_current.next
            current = current.next

        current.next = current.next.next
        return dummy.next