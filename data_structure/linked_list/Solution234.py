#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jim
@file: Solution234.py
@time: 2022/4/23 13:43
@Describe:
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """ 基于快慢指针

        :param head:
        :return:
        """
        while head is None:
            return False

        val_list = list()

        current_ = head
        while current_ is not None:
            val_list.append(current_.val)
            current_ = current_.next

        val_len = len(val_list)
        i, j = 0,val_len-1
        while i<= j:
            if val_list[i] == val_list[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        """ 快慢指针（需要注意边界问题）

        :param head:
        :return:
        """
        s = []
        slow = fast = head
        while fast is not None and fast.next is not None:
            s.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
            slow = slow.next

        while len(s) > 0:
            if slow.val != s.pop():
                return False
            slow = slow.next

        return True



if __name__ == "__main__":
    tmp1 = ListNode(2)
    tmp2 = ListNode(1,tmp1)
    solution = Solution()
    print(solution.isPalindrome(tmp2))

