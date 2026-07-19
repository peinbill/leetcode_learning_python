#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/7/18 22:49
# @Author      : Jim
# @File        : Solution206.py
# @Software    : PyCharm
# @Description :
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 非递归方法
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        current = dummy.next
        while current and current.next:
            next = current.next
            current.next = next.next
            next.next = dummy.next
            dummy.next = next
        return dummy.next

    # 递归方法
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归反转单链表
        :param head: 当前递归子链表的头节点
        :return: 反转完成后的新头节点（原链表尾节点）
        """
        # 递归终止条件1：当前节点为空，直接返回None（空链表）
        if head is None:
            return None
        # 递归终止条件2：当前节点是链表最后一个节点（无下一个节点）
        # 该节点就是反转后的整个链表的新头节点，直接返回
        if head.next is None:
            return head

        # 1. 递归处理后面的子链表
        # 传入head.next，把 head 之后的所有节点全部反转
        # new_head 永远保存反转完成后的链表头（原链表最后一个节点，全程不变）
        new_head = self.reverseList(head.next)

        # 2. 反转当前节点和后一个节点的指向（核心操作）
        # head.next 是后一个节点，让后一个节点的next指向当前head，完成反向
        head.next.next = head
        # 3. 断开当前节点原本向后的指针，防止链表循环
        # 如果不置空，会形成 A <-> B 的双向循环链表，死循环
        head.next = None

        # 4. 返回反转后的链表头节点（全程统一的尾部节点）
        return new_head
