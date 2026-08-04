#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/8/4 08:16
# @Author      : Jim
# @File        : Solution206.py
# @Software    : PyCharm
# @Description :
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 非递归方法
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        current = dummy.next
        while current and current.next:
            next = current.next
            current.next = next.next
            next.next = dummy.next
            dummy.next = next
        return dummy.next