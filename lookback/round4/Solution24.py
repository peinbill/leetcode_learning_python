#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/7 01:25
# @Author      : Jim
# @File        : Solution24.py
# @Software    : PyCharm
# @Description : 基于题义列出解即可

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        next = head.next
        next_next = next.next
        next.next = head
        head.next = self.swapPairs(next_next)

        return next