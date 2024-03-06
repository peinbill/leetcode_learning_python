#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/2/19 21:19
# @Author      : Jim
# @File        : Solution92.py
# @Software    : PyCharm
# @Description : 一种反转列表，核心在于画图画图画图

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy_node = ListNode(-1, head)

        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        current = pre.next

        for _ in range(right - left):
            next = current.next
            current.next = next.next
            next.next = pre.next
            pre.next = next

        return dummy_node.next