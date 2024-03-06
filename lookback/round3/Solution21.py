#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2024/1/3 21:49
# @Author      : Jim
# @File        : Solution21.py
# @Software    : PyCharm
# @Description : 数据结构——链表
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

        l1 = list1.val
        l2 = list2.val
        if l1 < l2:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2