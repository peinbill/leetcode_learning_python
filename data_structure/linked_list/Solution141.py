#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution141.py
@time: 2022/4/23 13:14
@Describe:
"""
# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     """
    #     需要画图 a,b,c 进行计算
    #     :param head:
    #     :return:
    #     """
    #     slow = fast = head
    #
    #     while fast is not None and fast.next is not None:
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #         if slow == fast:
    #             slow = head
    #             while fast != slow:
    #                 fast = fast.next
    #                 slow = slow.next
    #             return slow
    #
    #     return None


    def detectCycle2(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        fast,slow = head,head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True

        return False

    # def hasCycle2(self, head: Optional[ListNode]) -> bool:
    #     if head is None:
    #         return False
    #     current = head
    #     node_set = set()
    #     while current is not None:
    #         if current in node_set:
    #             return True
    #         else:
    #             node_set.add(current)
    #         current = current.next
    #
    #     return False