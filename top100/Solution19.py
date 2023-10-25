# -*- encoding: utf-8 -*-
"""
@File    : Solution19.py
@Time    : 2023/10/7 10:24 下午
@Author  : huangjinyu
@Desc   : 
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """ 哑节点+计算长度


        @param head:
        @param n:
        @return:
        """
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """ 需要画图，双指针方法

        @param head:
        @param n:
        @return:
        """
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next




