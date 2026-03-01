#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/3/1 20:11
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

        list1_val = list1.val
        list2_val = list2.val
        if list1_val < list2_val:
            next = self.mergeTwoLists(list1=list1.next, list2=list2)
        else:
            next = self.mergeTwoLists(list1=list1, list2=list2.next)

        return ListNode(val=min(list1_val, list2_val), next=next)
