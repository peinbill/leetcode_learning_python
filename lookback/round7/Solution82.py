from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     """ 一次遍历+哑结点应用

    #     :param head:
    #     :return:
    #     """
    #     if not head:
    #         return head

    #     dummy = ListNode(0, head)

    #     cur = dummy
    #     while cur.next and cur.next.next:
    #         if cur.next.val == cur.next.next.val:
    #             x = cur.next.val
    #             while cur.next and cur.next.val == x:
    #                 cur.next = cur.next.next
    #         else:
    #             cur = cur.next

    #     return dummy.next
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return head

        if head.next is None:
            return head

        def detect_duplicate_val(current):
            duplicate_set = set()
            next = current.next

            while current and next:
                if next.val == current.val:
                    duplicate_set.add(current.val)
                current = next
                next = next.next
            return duplicate_set

        duplicate_list = detect_duplicate_val(head)

        dummy = ListNode(next=head)

        pre = dummy
        current = dummy.next

        while current:
            if current.val in duplicate_list:
                pre.next = current.next
                current = current.next
            else:
                pre = current
                current = current.next

        return dummy.next