#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/2/20 00:01
# @Author      : Jim
# @File        : Solution206.py
# @Software    : PyCharm
# @Description : 206,基本上和92是配对的，搞定这两题，基本上反转链表问题就不大
# 核心还是在于画图
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)

        current = head
        while current and current.next:
            next = current.next

            current.next = next.next
            next.next = dummy_node.next

            dummy_node.next = next

        return dummy_node.next