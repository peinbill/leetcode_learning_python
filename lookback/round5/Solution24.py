#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/10 01:48
# @Author      : Jim
# @File        : Solution24.py
# @Software    : PyCharm
# @Description :

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        dummy = ListNode(next=head)


        current = head

        next = current.next
        next_next = next.next

        dummy.next = next

        next.next = current

        current.next = self.swapPairs(next_next)

        return dummy.next