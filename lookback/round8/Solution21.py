#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/2/18 18:02
# @Author      : Jim
# @File        : Solution21.py
# @Software    : PyCharm
# @Description :
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        val1 = list1.val
        val2 = list2.val

        if val1 < val2:
            list1.next = self.mergeTwoLists(list1=list1.next, list2=list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1=list1, list2=list2.next)
            return list2