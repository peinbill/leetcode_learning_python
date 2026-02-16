#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/16 10:39
# @Author      : Jim
# @File        : Solution24.py
# @Software    : PyCharm
# @Description :

from typing import List,Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def switch_node(node):
            if node and node.next:
                next = node.next
                node.next = switch_node(next.next)
                next.next = node

                return next
            else:
                return node
        node = switch_node(head)
        return node