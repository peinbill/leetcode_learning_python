# -*- encoding: utf-8 -*-
"""
@File    : Solution21.py
@Time    : 2023/10/8 8:55 上午
@Author  : huangjinyu
@Desc   : 
"""

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
            rtn = ListNode(val1)
            rtn.next = self.mergeTwoLists(list1.next, list2)
        else:
            rtn = ListNode(val2)
            rtn.next = self.mergeTwoLists(list1, list2.next)
        return rtn