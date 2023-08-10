#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution206.py
@time: 2022/4/20 22:13
@Describe:
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head

        pre = None

        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        return pre
