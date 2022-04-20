#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution1.py
@time: 2022/4/20 22:42
@Describe:
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ 哑结点+递归

        :param list1:
        :param list2:
        :return:
        """
        if list2 is None:
            return list1
        if list1 is None:
            return list2

        dummy = ListNode()

        if list1.val<list2:
            dummy.next = list1
            dummy.next.next = self.mergeTwoLists(list1.next,list2)
        else:
            dummy.next = list2
            dummy.next.next = self.mergeTwoLists(list1,list2.next)
        return dummy.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 双重哑结点做法

        :param l1:
        :param l2:
        :return:
        """
        tail = dummy = ListNode()
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next

        if l1 is None:
            tail.next = l2
        else:
            tail.next = l1

        return dummy.next