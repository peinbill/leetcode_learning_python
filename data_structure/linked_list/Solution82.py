#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution82.py
@time: 2022/4/18 21:04
@Describe:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """ 2次遍历+集合+头结点

        :param head:
        :return:
        """
        if head is None:
            return head

        current = head

        duplicate_set = set()

        while current.next is not None:
            if current.val == current.next.val:
                duplicate_set.add(current.val)

                current.next = current.next.next
            else:
                current = current.next

        ans = ListNode()
        current_ans = ans

        current = head
        while current is not None:
            if current.val in duplicate_set:
                current = current.next
            else:
                current_ans.next = ListNode(current.val)
                current_ans = current_ans.next
                current = current.next

        return ans.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        """ 一次遍历+哑结点应用

        :param head:
        :return:
        """
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next



