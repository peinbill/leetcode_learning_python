#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2026/5/6 21:18
# @Author      : Jim
# @File        : Solution25.py
# @Software    : PyCharm
# @Description :
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 翻转 [head, tail] 区间的链表
    # 返回：翻转后的新头结点、新尾结点
    def reverse(self, head: ListNode, tail: ListNode):
        # 前驱初始化为 tail 的下一个节点（当作翻转后的尾部后继）
        prev = tail.next
        # 从区间头节点开始遍历
        p = head
        # 循环终止条件：前驱走到 tail，代表全部翻转完成
        while prev != tail:
            # 保存当前节点的下一个节点
            nex = p.next
            # 当前节点指向前驱，完成局部反转
            p.next = prev
            # 前驱后移
            prev = p
            # 指针后移，处理下一个节点
            p = nex
        # 翻转后：原tail变新头，原head变新尾
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 虚拟头节点，统一链表边界操作，避免单独处理头部
        hair = ListNode(0)
        hair.next = head
        # pre：待翻转区间的前驱节点
        pre = hair

        # 只要还有节点，就循环分组翻转
        while head:
            # 先定位当前组的尾节点
            tail = pre
            # 向后走 k 步，截取 k 个节点为一组
            for i in range(k):
                tail = tail.next
                # 中途为空，说明剩余节点不足 k 个，直接返回结果
                if not tail:
                    return hair.next

            # 保存下一组的起始节点，翻转后需要衔接
            nex = tail.next
            # 翻转当前 [head, tail] 区间
            head, tail = self.reverse(head, tail)

            # 将翻转后的组，重新接入原链表
            pre.next = head
            # 当前组尾连接下一组开头
            tail.next = nex

            # 更新指针，处理下一组
            pre = tail
            head = tail.next

        return hair.next