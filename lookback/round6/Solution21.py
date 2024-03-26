#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/3/16 08:11
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

        l1_val = list1.val
        l2_val = list2.val

        if l1_val < l2_val:
            next = self.mergeTwoLists(list1.next,list2)
            return ListNode(l1_val,next)
        else:
            next = self.mergeTwoLists(list1,list2.next)
            return ListNode(l2_val,next)
