# -*- encoding: utf-8 -*-
"""
@File    : Solution142.py
@Time    : 2023/7/30 4:34 下午
@Author  : huangjinyu
@Desc   : 
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ans = head
                while ans != slow:
                    ans = ans.next
                    slow = slow.next
                return ans
        return None