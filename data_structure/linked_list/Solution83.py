#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution83.py
@time: 2022/4/18 20:57
@Describe:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """ 遍历，考察链表的基本操作

        :param head:
        :return:
        """

        if head is None:
            return head

        current = head

        while current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head